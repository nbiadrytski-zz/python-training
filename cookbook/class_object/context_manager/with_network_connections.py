from socket import socket, AF_INET, SOCK_STREAM


class LazyConnections:
    def __init__(self, addr, family=AF_INET, type=SOCK_STREAM):
        self.family = family
        self.addr = addr
        self.type = type
        self.connections = []

    def __enter__(self):  # create socket connections and add to the stack
        sock = socket(self.family, self.type)
        sock.connect(self.addr)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):  # pops the last connection off the stack and closes it
        self.connections.pop().close()
