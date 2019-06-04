import argparse, socket
from datetime import datetime
# UDP client and server on localhost

MAX_BYTES = 65535


def server(port):
    # SOCK_DGRAM datagram type, which means it will use UDP on an IP network
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # family is AF_INET, the Internet family of protocols
    sock.bind(('127.0.0.1', port))  # UDP network address
    print(f'Listening at {sock.getsockname()}')
    while True:
        # server repeatedly runs recvfrom(),
        # telling the routine that it will receive messages up to a maximum length of 65,535 bytes
        # Until you send a message with a client, your recvfrom() call will wait forever
        # Once a datagram arrives,
        # recvfrom() will return the address of the client that sent you a datagram and the datagram’s contents as bytes
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        # print the message to the console
        print('The client at {} says {!r}'.format(address, text))
        text = f'Your data was {len(data)} bytes long'
        data = text.encode('ascii')
        # return a reply datagram to the client
        sock.sendto(data, address)


def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = f'The time is {datetime.now()}'
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))  # message and a destination address
    print(f'The OS assigned me (client) the address {sock.getsockname()}')
    data, address = sock.recvfrom(MAX_BYTES)
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)


