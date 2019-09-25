import sys

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet.serialport import SerialPort
from twisted.python import log

log.startLogging(sys.stdout)
client_list = []  # TCP clients connecting to me
usb_list = []


class USBClient(Protocol):

    def __init__(self, network):
        self.network = network
        self.usb_list = []

    def connectionFailed(self):
        print("Connection Failed:", self)
        reactor.stop()

    def connectionMade(self):
        """Called when the connection is completed."""
        usb_list.append(self)
        print('Connected to Bridge')
        USBClient.send_line(self, b'ls')

    def dataReceived(self, data):
        """Called whenever data is received."""
        print("Data received: ", repr(data))
        #print("Data received! with %d bytes!" % len(data))

        # for cli in client_list:
        #     print(cli)
        #     cli.transport.readline().decode('utf-8')
        #self.network.notifyAll(data)  # !!AArgh..!Could not get this to work
        self.network.notifyAll(data)
        pass

    # def lineReceived(self, line):
    #     print("Line received", repr(line))

    def send_line(self, cmd):
        self.transport.write(cmd)

    def outReceived(self, data):
        print("outReceived! with %d bytes!" % len(data))
        self.data = self.data + data


class CommandRx(Protocol):

    def connectionMade(self):
        print('Connection received from tcp..')
        client_list.append(self)

    def dataReceived(self, data):
        print('Command receive', repr(data))
        for usb in usb_list:
            usb.transport.write(data)

    def connectionLost(self, reason):
        print('Connection lost', reason)
        if self in client_list:
            print("Removing " + str(self))
            client_list.remove(self)


class CommandRxFactory(Factory):
    protocol = CommandRx

    def __init__(self):
        self.client_list = []

    def notifyAll(self, data):
        for cli in self.client_list:
            cli.transport.write(data)


if __name__ == '__main__':
    tcpfactory = CommandRxFactory()

    reactor.listenTCP(65432, tcpfactory)
    SerialPort(USBClient(tcpfactory), '/dev/tty.usbserial-14200', reactor, baudrate='115200')
    reactor.run()
