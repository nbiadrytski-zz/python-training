from functools import partial
from cookbook.class_object.context_manager.with_network_connections import LazyConnections


conn = LazyConnections(("www.python.org", 80))

with conn as s1:
    # conn.__enter__() executes: connection open
    s1.send(b'GET /index.html HTTP/1.0\r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    resp1 = b''.join(iter(partial(s1.recv, 8192), b''))
    print(resp1)
    # conn.__exit__() executes: connection closed
    with conn as s2:
        s2.send(b'GET /index.html HTTP/1.0\r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        resp2 = b''.join(iter(partial(s1.recv, 8192), b''))
