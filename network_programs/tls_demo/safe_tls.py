import argparse, socket, ssl


def client(host, port, cafile=None):
    purpose = ssl.Purpose.SERVER_AUTH  # verify the server to which clients connect
    context = ssl.create_default_context(purpose, cafile=cafile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((host, port))
        print(f'Client {client_sock.getsockname()} connected to server {host!r}:{port}')
        ssl_sock = context.wrap_socket(client_sock, server_hostname=host)

        with ssl_sock:
            while True:
                data = ssl_sock.recv(1024)
                if not data:
                    break
                print(repr(data))


def server(host, port, certfile, cafile=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.load_cert_chain(certfile)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(1)
        print(f'Server listening at interface {host!r}:{port}')
        connection_sock, address = listener.accept()
        print(f'Server accepted a connection from client {address!r}')

        with connection_sock:
            ssl_sock = context.wrap_socket(connection_sock, server_side=True)

            with ssl_sock:
                ssl_sock.sendall('Simple is better than complex.'.encode('ascii'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Safe TLS client and server')
    parser.add_argument('host', help='hostname or IP address')
    parser.add_argument('port', type=int, help='TCP port number')
    parser.add_argument('-a', metavar='cafile', default=None, help='authority: path to CA certificate PEM file')
    parser.add_argument('-s', metavar='certfile', default=None, help='run as server: path to server PEM file')
    args = parser.parse_args()

    if args.s:
        server(args.host, args.port, args.s, args.a)
    else:
        client(args.host, args.port, args.a)

# run server: python3 safe_tls.py -s localhost.pem '' 1060
# run client: python3 safe_tls.py -a ca.crt localhost 1060
# the above tells the client to trust localhost.pem certificate that ca.crt has signed.
# listen to TCP traffic: sh-3.2# tcpdump -n port 1060 -i lo0 -X
