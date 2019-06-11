import socket


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # connect to server
    client_socket.sendall(b'Hello, world')  # send message to server
    # 1024 is the maximum amount of data to be received at once
    data = client_socket.recv(1024)  # read server's reply

print(f'Client received {repr(data)}')