import socket

# IP Addresses (130.207.244.244):
# four decimal numbers, separated by periods, which each represent a single byte of the address.
# Each number can therefore range from 0 to 255.
# Every byte in an IP address represents eight bits of binary data.
# To read subnet numbers:
# 127.0.0.0/8: the first 8 bits (1 byte) must match the number 127
# and that the remaining 24 bits (3 bytes) can have any value they want

# 192.168.0.0/16: This pattern will match any IP address that belongs in the private 192.168 range
# because the first 16 bits must match perfectly.
# The last 16 bits of the 32-bit address are allowed to have whatever value they want.

# 192.168.5.0/24: The first three bytes of the address are completely specified,
# and they have to match for an IP address to fall into this range.
# Only the last byte (the last eight bits) is allowed to vary between machines in this range.
# This leaves 256 unique addresses.

if __name__ == '__main__':
    hostname = 'maps.google.com'
    addr = socket.gethostbyname(hostname)
    print('The IP address of {} is {}'.format(hostname, addr))  # The IP address of maps.google.com is 216.58.207.46

    print(socket.getservbyname('domain'))  # 53, get DNS port

