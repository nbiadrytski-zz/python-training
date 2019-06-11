import socket


try:
    print('Fully qualified domain name: ' + socket.getfqdn('8.8.8.8'))  # google-public-dns-a.google.com
    print('Host name to ip address: ' + socket.gethostbyname('www.python.org'))  # 151.101.64.223
    print('Host name to ip address, extended: ' + str(socket.gethostbyname_ex('www.python.org')))
    # ('dualstack.python.map.fastly.net', --> hostname
    # ['www.python.org'], --> domain name
    # ['151.101.64.223', '151.101.128.223', '151.101.192.223', '151.101.0.223']) --> ip addresses
    print('Local machine hostname: ' + socket.gethostname())  # EPBYMINW3204
except Exception as err:
    print('Error: ' + str(err))