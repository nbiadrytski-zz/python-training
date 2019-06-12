import argparse, socket, time


aphorisms = {b'Beautiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}


def get_answer(aphorism):
    """Return the string response to a particular Zen-of-Python aphorism."""
    time.sleep(0.0)
    return aphorisms.get(aphorism, b'Error: unknown aphorism.')


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print(f'Server listening at {address}')
    return listener


def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        connection_sock, client_address = listener.accept()
        print(f'Client {client_address} connected to server {connection_sock.getsockname()}')
        handle_conversation(connection_sock, client_address)


def handle_conversation(sock, address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_request(sock)
    # client has finished making requests and has finally hung up which is normal and not a truly an exceptional event
    except EOFError:
        print(f'Client {address} finished making requests and has closed')
    except Exception as e:
        print(f'Client {address} error: {e}')
    finally:
        sock.close()  # make sure that the client socket is always closed


def handle_request(sock):
    """Receive a single client request on `sock` and send the answer."""
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)  # sendall() guarantees the delivery of an entire payload


def recv_until(sock, suffix):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        # Repeated calls are made to the socket’s recv()
        # until the accumulated byte string finally qualifies as a complete question.
        data = sock.recv(4096)
        if not data:
            raise IOError(f'received {message!r}, then socket closed')
        message += data
    return message
