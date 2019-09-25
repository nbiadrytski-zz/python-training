import sys

from twisted.internet import reactor, protocol, serialport
from twisted.python import log


log.startLogging(sys.stdout)


class SerialPort(protocol.Protocol):
    """
    Create a serial port connection.
    Pass data from it to a known list of TCP ports.
    """

    def __init__(self, port, reactor, baudrate):
        self.tcp_ports = []
        self.serial = serialport.SerialPort(self, reactor, port, baudrate, rtscts=0)
        self.serial.registerProducer(self, True)
        self.paused = False

    def add_tcp(self, tcp_port):
        """Add TCP port to those receiving serial data."""
        if self.paused:
            tcp_port.transport.pauseProducing()
        self.tcp_ports.append(tcp_port)

    def del_tcp(self, tcp_port):
        """Remove TCP port from the those receiving serial data."""
        self.tcp_ports.remove(tcp_port)

    def write(self, data):
        """Write data to the serial port."""
        self.serial.write(data)

    def pauseProducing(self):
        """Pause producing event"""
        print("pausing producing")
        self.paused = True
        for port in self.tcp_ports:
            port.transport.pauseProducing()

    def resumeProducing(self):
        """Resume producing event"""
        print("resumimg producing")
        self.paused = False
        for port in self.tcp_ports:
            port.transport.resumeProducing()

    def stopProducing(self):
        """Stop producing event"""
        print("stopping producing")

    def connectionMade(self):
        """Called when the connection is completed."""
        print('Connected to Bridge')
        self.write(b'test')

    def dataReceived(self, data):
        """Pass any received data to the list of TCPPorts."""
        print(repr(data))
        for tcp_port in self.tcp_ports:
            tcp_port.write(data)
            print(data)


class TCPPort(protocol.Protocol):
    """Create a TCP server connection and pass data from it to the serial port."""

    def __init__(self, serial):
        """Add this TCPPort to the SerialPort."""
        self.serial = serial
        self.serial.add_tcp(self)

    def __del__(self):
        """Remove this TCPPort from the SerialPort."""
        self.serial.del_tcp(self)

    def dataReceived(self, data):
        """Pass received data to the SerialPort."""
        print("write", len(data))
        self.serial.write(data)

    def write(self, data):
        """Write data to the TCP port."""
        self.transport.write(data)
        print('wrote data')


class TCPPortFactory(protocol.ServerFactory):
    """
    Factory to create TCPPort protocol instances.
    Instanced SerialPort must be passed in.
    """

    def __init__(self, serial):
        self.serial = serial
        self.index = 0

    def buildProtocol(self, addr):
        """Build TCPPort, passing in the instanced SerialPort."""
        p = TCPPort(self.serial)
        self.index += 1
        p.factory = self
        return p


def main():
    # """Parse the command line and run the UI"""
    # try:
    #     opts, args = getopt.getopt(sys.argv[1:], "hp:b:t:lL:",
    #                                ["help", "port=", "baud=", "tcp=", "log", "log_name="])
    # except getopt.GetoptError as e:
    #     print(e)
    #     sys.exit(2)
    # tty_port = 0
    # baudrate = 9600
    # tcp_port = 1234
    serial_port = SerialPort(reactor, '/dev/tty.usbserial-14200', 115200)
    #serial_port.write(b'hello')
    tcp_port_factory = TCPPortFactory(serial_port)
    reactor.listenTCP(65432, tcp_port_factory)
    reactor.run()


if __name__ == "__main__":
    main()
