import socket


def main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)  # listen for 1 connection
    conn, addr = s.accept()  # accept connection
    print("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024)  # receive not more that 1024 bytes
        if not data:
            break
        print("From connected user: " + str(data))
        data = str(data).upper()
        print("Sending: " + str(data))
        conn.send(bytearray(data, 'utf-8'))
    conn.close()


if __name__ == "__main__":
    main()

