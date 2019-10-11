import os.path
import time
import sys
import re

import paramiko


# Checking username/password file
# Prompting user for input - USERNAME/PASSWORD FILE
user_file = input('\nEnter user file path and name: ')

# Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file):
    print('\nUsername/password file is valid.\n')
else:
    print('\nFile {} does not exist... Please check and try again.\n'.format(user_file))
    sys.exit()

# Checking commands file
# Prompting user for input - COMMANDS FILE
cmd_file = input('\n# Enter commands file path and name: ')

# Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file):
    print('\nCommand file is valid.\n')
else:
    print('\nFile {} does not exist... Please check and try again.\n'.format(cmd_file))
    sys.exit()


def ssh_connection(ip):

    global user_file
    global cmd_file

    try:
        with open(user_file, 'r') as selected_user_file:
            # Starting from the beginning of the file
            selected_user_file.seek(0)
            # Reading the username from the file
            username = selected_user_file.readlines()[0].split(',')[0].rstrip('\n')
            # Starting from the beginning of the file
            selected_user_file.seek(0)
            # Reading the password from the file
            password = selected_user_file.readlines()[0].split(',')[1].rstrip('\n')

        with paramiko.SSHClient() as session:
            # Allows auto-accepting unknown host keys
            session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the device using username and password
            session.connect(ip.rstrip('\n'), username=username, password=password)

            # Start an interactive shell session on the router
            connection = session.invoke_shell()
            time.sleep(1)
            # Setting terminal length for entire output - disable pagination
            connection.send('enable\n')
            connection.send('terminal length 0\n')
            time.sleep(1)
            # Entering global config mode
            connection.send('\n')
            connection.send('configure terminal\n')
            time.sleep(1)

            with open(cmd_file, 'r') as selected_cmd_file:
                # Starting from the beginning of the file
                selected_cmd_file.seek(0)
                # Writing each line (command) in the file to the device
                for each_line in selected_cmd_file.readlines():
                    connection.send(each_line + '\n')
                    time.sleep(2)

            # Checking command output
            command_output = connection.recv(65535)  # 65535 max number of bytes
            if re.search(b'% Invalid input', command_output):
                print('There was at least one IOS syntax error on device {} ...'.format(ip))
            else:
                print('\nDONE for device {}\n'.format(ip))
            # Print command output decoded from bytes
            # print(command_output.decode('utf-8'))
            print(re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(command_output))[1])

    except paramiko.AuthenticationException:
        print('Invalid username or password...\nPlease check username/password file or the device configuration.')
        print('Closing program... Bye!')
