import argparse, random, socket
import network_programs.server_architecture.zen_utils as z_utils


def client(address, cause_error=False):
    """
    In the normal case, where cause_error is False, this client creates a TCP socket and transmits three aphorisms,
    waiting after each one for the server to reply with an answer.
    In case you want to see what any of the servers do in the case of an error,
    the -e option to this client will make it send an incomplete question and then hang up abruptly on the server.
    """
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(address)
    aphorisms = list(z_utils.aphorisms)
    if cause_error:
        client_sock.sendall(aphorisms[0][:-1])
        return
    for aphorism in random.sample(aphorisms, 3):
        client_sock.sendall(aphorism)
        print(aphorism, z_utils.recv_until(client_sock, b'.'))
    client_sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    client(address, args.e)
