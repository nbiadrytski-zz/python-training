import network_programs.server_architecture.zen_utils as z_utils
from threading import Thread


# Using multiple threads to serve several clients in parallel.


def start_threads(listener, workers=4):
    t = (listener,)
    for i in range(workers):
        Thread(target=z_utils.accept_connections_forever, args=t).start()


if __name__ == '__main__':
    address = z_utils.parse_command_line('multi-threaded server')
    listener = z_utils.create_srv_socket(address)
    start_threads(listener)
