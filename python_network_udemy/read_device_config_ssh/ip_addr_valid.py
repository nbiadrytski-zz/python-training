import sys
import socket


def ip_addr_valid(ip_list):
    for ip in ip_list:
        # remove newline char from the end of each ip
        ip = ip.rstrip('\n')

        # OSError will be raise if ip is invalid
        try:
            socket.inet_aton(ip)
            print('{} ip address is valid according to socket.inet_aton()'.format(ip))
        except OSError as e:
            print('{} ip address is not valid: {}'.format(ip, e))
            sys.exit()

        # split each ip into ['10','10','10','2']
        octet_list = ip.split('.')

        # validate ips according to internal rules, not:
        # loopback, multicast, broadcast, link-local, reserved for future use
        if (len(octet_list) == 4) and \
                (1 <= int(octet_list[0]) <= 223) and \
                (int(octet_list[0]) != 127) and \
                (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and \
                (0 <= int(octet_list[1]) <= 255 and
                 0 <= int(octet_list[2]) <= 255 and
                 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print('\nThere was an invalid IP address in the file: {}\n'.format(ip))
            sys.exit()
