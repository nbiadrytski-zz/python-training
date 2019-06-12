import network_programs.server_architecture.zen_utils as z_utils

# Single-threaded server that serves one client at a time; others must wait.


if __name__ == '__main__':
    address = z_utils.parse_command_line('simple single-threaded server')
    listener = z_utils.create_srv_socket(address)
    z_utils.accept_connections_forever(listener)


