import argparse, socket


# In most real-world programs, the loop that runs recv() is more complicated
# because a program often has to read or process part of the message before it can guess how much more is coming
# E.g. HTTP response consists of headers, blank line,
# and then however many further bytes of data were specified in the Content-Length header
# You do not know how many times to keep running recv()
# until you had at least received the headers and then parsed them to find out the content length
def recvall(sock, length):
    data = b''  # <class 'bytes'>
    # wait until all 16 bytes are received
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError(
                f'was expecting {length} bytes but only received {len(data)} bytes before the socket closed')
        data += more
        return data


# run as "python3 tcp_sixteen.py server ""
# bind() tells the operating system what are the network interfaces from which you are willing to receive connections
# if you run server with an empty string for the hostname,
# which tells Python bind() routine
# that you are willing to accept connections through any of your machine’s active network interfaces
# 0.0.0.0 to mean “accept connections on any interface”
def server(interface, port):
    # bring up the server, run the client against it, and then try killing and rerunning the server
    # OSError: [Errno 98] Address already in use
    # The answer is that once a connected TCP connection is finally closed,
    # operating system’s network stack actually keeps a record of it around for up to four minutes in a waiting state.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))  # claims a particular port on a particular interface
    # After listen() has been called, the socket now cannot send or receive data.
    # this socket will now never be connected to any specific client.
    # Instead, the socket can now be used only to receive incoming connections through its accept() method
    sock.listen(1)  # 1 is number of waiting connections allowed
    print(f'Server listening at {sock.getsockname()}')  # listening (passive) socket: ('0.0.0.0', 1060)
    while True:
        print('Server waiting to accept a new connection')
        # waits for a new client to connect
        # then returns new socket that governs the new conversation that has just started
        sc, sockname = sock.accept()
        print(f'Server accepted a connection from client with {sockname}')
        print(f'  Socket name: {sc.getsockname()}')  # new active (connected) socket: Socket name: ('127.0.0.1', 1060)
        print(f'  Socket peer (client): {sc.getpeername()}')  # ('127.0.0.1', 65424)
        message = recvall(sc, 16)
        print(f'  Incoming sixteen-octet message: {repr(message)}')
        sc.sendall(b'Farewell, client')
        sc.close()
        print('  Reply sent, socket closed')


# run as "python3 tcp_sixteen.py client 127.0.0.1"
def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))  # connect to server
    print(f'Client has been assigned socket name {sock.getsockname()}')  # ('127.0.0.1', 65424)
    # sendall() makes sure the whole stream was sent
    # as network card may be busy or its buffer is almost full (which queues part of the stream)
    sock.sendall(b'Hi there, server')
    reply = recvall(sock, 16)
    print(f'The server said {repr(reply)}')
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at; host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
