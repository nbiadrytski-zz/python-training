import sys

from python_network_udemy.read_device_config_ssh.ip_file_valid import ip_file_valid
from python_network_udemy.read_device_config_ssh.ip_addr_valid import ip_addr_valid
from python_network_udemy.read_device_config_ssh.ip_reach import ip_reach
from python_network_udemy.read_device_config_ssh.ssh_connection import ssh_connection
from python_network_udemy.read_device_config_ssh.create_threads import create_threads


# Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print('\n\nProgram aborted by user. Exiting...\n')
    sys.exit()

# Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)
except KeyboardInterrupt:
    print('\n\nProgram aborted by user. Exiting...\n')
    sys.exit()

# Calling threads creation function for one or multiple SSH connections
create_threads(ip_list, ssh_connection)

