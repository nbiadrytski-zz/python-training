import os.path
import sys


def ip_file_valid():
    """Check IP address file and content validity."""
    ip_file = input('\n# Enter IP file path and name: ')
    # check if file is valid
    if os.path.isfile(ip_file):
        print('\n* IP file is valid :)\n')
    else:
        print('\n* File {} does not exist... Please check and try again.\n'.format(ip_file))
        sys.exit()

    # Open user selected file for reading (IP addresses file)
    with open(ip_file, 'r') as selected_ip_file:
        # Starting from the beginning of the file
        selected_ip_file.seek(0)
        # Reading each line (IP address) in the file
        ip_list = selected_ip_file.readlines()

    return ip_list
