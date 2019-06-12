import select
import network_programs.server_architecture.zen_utils as z_utils


def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event


def serve(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        # Socket closed: remove it from our data structures.
        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print(f'Client {address} sent {rb} but then closed')
            elif sb:
                print(f'Client {address} closed before we sent {sb}')
            else:
                print(f'Client {address} closed socket normally')
            poll_object.unregister(fd)
            del sockets[fd]

        # New socket: add it to our data structures.
        elif sock is listener:
            sock, address = sock.accept()
            print(f'Server accepted connection from {address}')
            sock.setblocking(False)  # force socket.timeout if we made a mistake
            sockets[sock.fileno()] = sock
            addresses[sock] = address
            poll_object.register(sock, select.POLLIN)

        # Incoming data: keep receiving until we see the suffix.
        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:  # end-of-file
                sock.close()  # next poll() will POLLNVAL, and thus clean up
                continue
            data = bytes_received.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                bytes_to_send[sock] = z_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data

        # Socket ready to send: keep sending until all bytes are delivered.
        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


if __name__ == '__main__':
    address = z_utils.parse_command_line('low-level async server')
    listener = z_utils.create_srv_socket(address)
    serve(listener)









