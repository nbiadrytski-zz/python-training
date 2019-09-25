import socket
import serial.threaded
import sys


class SerialToNet(serial.threaded.Protocol):
    """serial->socket"""

    def __init__(self):
        self.socket = None

    def __call__(self):
        return self

    def data_received(self, data):
        if self.socket is not None:
            print(f'Ethernet Bridge received "{data.decode("utf-8")}" from TCP client')
            self.socket.sendall(data)


# /dev/tty.usbserial-14200
bridge = serial.serial_for_url('/dev/serial/by-id/usb-FTDI_Dual_RS232-HS-if00-port0', 115200)
serial_to_tcp = SerialToNet()
serial_worker = serial.threaded.ReaderThread(bridge, serial_to_tcp)
serial_worker.start()


HOST = '127.0.0.1'
PORT = 65432

# AF_INET - address family, SOCK_STREAM - socket type for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
    # bring up the server, run the client against it, and then try killing and rerunning the server
    # OSError: [Errno 98] Address already in use
    # The answer is that once a connected TCP connection is finally closed,
    # operating system’s network stack actually keeps a record of it around for up to four minutes in a waiting state.
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind() tells your OS what are the network interfaces from which you are willing to receive connections
    # if you run server with an empty string for the hostname,
    # which tells Python bind() routine
    # that you are willing to accept connections through any of your machine’s active network interfaces
    # 0.0.0.0 to mean “accept connections on any interface”
    listen_socket.bind((HOST, PORT))
    # listen() enables a server to accept() connections. It makes it a “listening” socket.
    listen_socket.listen(1)  # 1 is number of waiting connections allowed
    # connection_socket is the socket to communicate with the client
    connection_socket, client_address = listen_socket.accept()  # blocks and waits for an incoming connection
    print(f'TCP client {client_address} '
          f'connected to TCP Server {connection_socket.getsockname()} '
          f'at serial port "{bridge.portstr}"')
    try:
        serial_to_tcp.socket = connection_socket  # enter network <-> serial loop
        while True:
            try:
                # receiving data from client socket
                data = connection_socket.recv(2048)
                if not data:
                    break
                bridge.flush()  # flush before sending data
                bridge.write(data)  # serial sends received data back to tcp client
                print(f'Ethernet Bridge sent: "{data.decode("utf-8")}" to TCP client')
            except socket.error as msg:
                sys.stderr.write('ERROR: {}\n'.format(msg))
                break
    except socket.error as msg:
        sys.stderr.write('ERROR: {}\n'.format(msg))

serial_worker.stop()
