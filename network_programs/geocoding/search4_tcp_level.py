import socket
import ssl
from urllib.parse import quote_plus

# HTTP protocol operates by dictating exactly what the text of the messages will look like
# that pass back and forth between two hosts that can speak TCP.

# TCP sends a raw text message across the Internet and receives a bundle of text in return


request_text = """\
GET /search?q={}&format=json HTTP/1.1\r\n\
Host: nominatim.openstreetmap.org\r\n\
User-Agent: test\r\n\
Connection: close\r\n\
\r\n\
"""


def geocode(address):
    # calling the raw socket() function that is provided by the host operating system
    # to support basic network communications on an IP network
    unencrypted_sock = socket.socket()
    unencrypted_sock.connect(('nominatim.openstreetmap.org', 443))
    sock = ssl.wrap_socket(unencrypted_sock)
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        if not more:
            break
        raw_reply += more
    print(raw_reply.decode('utf-8'))


if __name__ == '__main__':
    geocode('207 N. Defiance St, Archbold, OH')

