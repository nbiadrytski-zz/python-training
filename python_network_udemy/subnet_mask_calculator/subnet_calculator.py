import random
import sys
import socket


masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
no_of_zeros = 0
no_of_ones = 0
no_of_hosts = 0
bst_ip_address = []
net_ip_address = []


def validate_ip():
    while True:
        ip_address = input('Enter an IP address: ')
        ip_octets = ip_address.split('.')
        try:  # OSError will be raised if ip is invalid
            socket.inet_aton(ip_address)
            print(f'{ip_address} ip address is valid according to socket.inet_aton()')
            return ip_octets
        except OSError as e:
            print(f'{ip_address} ip address is not valid. Error: {e}')
            continue


def validate_mask():
    while True:
        subnet_mask = input('Enter a subnet mask: ')
        # Checking octets
        mask_octets = subnet_mask.split('.')
        if (len(mask_octets) == 4) and \
                (int(mask_octets[0]) == 255) and \
                (int(mask_octets[1]) in masks) and \
                (int(mask_octets[2]) in masks) and \
                (int(mask_octets[3]) in masks) and \
                (int(mask_octets[0]) >=
                 int(mask_octets[1]) >=
                 int(mask_octets[2]) >=
                 int(mask_octets[3])):
            return mask_octets
        else:
            print('\nThe subnet mask is INVALID! Please retry!\n')
            continue


def get_wildcard_mask(mask_octs):
    """Algorithm for subnet identification, based on IP and Subnet Mask"""
    # Convert mask to binary string
    mask_octets_binary = []
    for octet in mask_octs:
        binary_octet = bin(int(octet)).lstrip('0b')
        mask_octets_binary.append(binary_octet.zfill(8))
    # Example: for 255.255.255.0 => 11111111111111111111111100000000
    binary_mask = ''.join(mask_octets_binary)
    # Counting host bits in the mask and calculating number of hosts/subnet
    global no_of_zeros
    global no_of_ones
    global no_of_hosts
    no_of_zeros = binary_mask.count('0')
    no_of_ones = 32 - no_of_zeros
    no_of_hosts = abs(2 ** no_of_zeros - 2)  # return a positive value for the /32 mask (all 255s)
    # Obtaining wildcard mask
    wildcard_octets = []
    for octet in mask_octs:
        wild_octet = 255 - int(octet)
        wildcard_octets.append(str(wild_octet))
    wildcard_mask = '.'.join(wildcard_octets)
    return wildcard_mask


def convert_ip_to_binary_str(ip_octets):
    ip_octets_binary = []
    for octet in ip_octets:
        binary_octet = bin(int(octet)).lstrip('0b')
        ip_octets_binary.append(binary_octet.zfill(8))
    binary_ip = "".join(ip_octets_binary)
    return binary_ip  # for 192.168.2.100 => 11000000101010000000101000000001


def get_network_address_binary(binary_ip):
    network_address_binary = binary_ip[:no_of_ones] + '0' * no_of_zeros
    return network_address_binary


def get_broadcast_address_binary(binary_ip):
    broadcast_address_binary = binary_ip[:(no_of_ones)] + "1" * no_of_zeros
    return broadcast_address_binary


def convert_network_address_back_to_decimal(network_address_binary):
    net_ip_octets = []
    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        net_ip_octet = network_address_binary[bit: bit + 8]
        net_ip_octets.append(net_ip_octet)
    global net_ip_address
    for each_octet in net_ip_octets:
        net_ip_address.append(str(int(each_octet, 2)))
    network_address = '.'.join(net_ip_address)
    return network_address


def convert_broadcast_address_back_to_decimal(broadcast_address_binary):
    bst_ip_octets = []
    # range(0, 32, 8) means 0, 8, 16, 24
    for bit in range(0, 32, 8):
        bst_ip_octet = broadcast_address_binary[bit: bit + 8]
        bst_ip_octets.append(bst_ip_octet)
    global bst_ip_address
    for each_octet in bst_ip_octets:
        bst_ip_address.append(str(int(each_octet, 2)))
    broadcast_address = ".".join(bst_ip_address)
    return broadcast_address


def generate_random_ip_in_subnet():
    while True:
        generate = input('Generate random IP address from this subnet? (y/n)')
        if generate == 'y':
            generated_ip = []

            # Obtain available IP address in range
            # based on the difference between octets in broadcast address and network address
            for indexb, oct_bst in enumerate(bst_ip_address):
                for indexn, oct_net in enumerate(net_ip_address):
                    if indexb == indexn:
                        if oct_bst == oct_net:
                            # Add identical octets to the generated_ip list
                            generated_ip.append(oct_bst)
                        else:
                            # Generate random number(s) from within octet intervals and append to the list
                            generated_ip.append(str(random.randint(int(oct_net), int(oct_bst))))

            # IP address generated from the subnet pool
            y_iaddr = ".".join(generated_ip)

            print('Random IP address is: %s' % y_iaddr)
            continue
        else:
            print('Ok, bye!')
            break


if __name__ == '__main__':
    try:
        ip_octs = validate_ip()
        mask_octets = validate_mask()
        wild_mask = get_wildcard_mask(mask_octets)

        bin_ip = convert_ip_to_binary_str(ip_octs)

        network_address_bin = get_network_address_binary(bin_ip)
        broadcast_address_bin = get_broadcast_address_binary(bin_ip)

        net_address = convert_network_address_back_to_decimal(network_address_bin)
        brst_address = convert_broadcast_address_back_to_decimal(broadcast_address_bin)

        # Results for selected IP/mask
        print('Network address is: %s' % net_address)
        print('Broadcast address is: %s' % brst_address)
        print('Number of valid hosts per subnet: %s' % no_of_hosts)
        print('Wildcard mask: %s' % wild_mask)
        print('Mask bits: %s' % no_of_ones)

        generate_random_ip_in_subnet()

    except KeyboardInterrupt:
        print('\n\nProgram aborted by user. Exiting...\n')
        sys.exit()
