import paramiko
import time

test = 'dkfjbvdjkfb ekjbgdjbg ejrbjkebrg ekjbrgekjbrgejkbrg ekjregknjbrngjkebr kejrbgkjerbgejkrbg ekjrbgejkbgejkrbg kejrbgejkbrg'
HOST = '10.6.221.128'
USERNAME = 'pyauto'
PASSWORD = 'PythonMentoringBY2019'

upload_local_path = '/Users/mikalai_biadrytski/Desktop/in.txt'
upload_remote_path = '/home/pyauto/in.txt'
download_remote_path = '/home/pyauto/out.txt'
download_local_path = '/Users/mikalai_biadrytski/Desktop/out.txt'


def connect_to_remote_host(host, username, password):
    """Establish SSH connection to remote VM"""
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.connect(host, username=username, password=password)
    return ssh_client


def create_sftp_client(ssh_client):
    """Create SFTP client to upload/download files based on created SSH client"""
    sftp_client = ssh_client.open_sftp()
    return sftp_client


def run_ls_command(ssh_client):
    """Run ls command in current directory and output result"""
    _, current_dir, _ = ssh_client.exec_command('pwd')
    _, stdout, _ = ssh_client.exec_command('ls')
    print(f'Directory {current_dir.read().decode("utf-8")[:-1]} contains:')
    for idx, line in enumerate(stdout):
        print(f'{idx}. {line}')


def run_curl_command(ssh_client):
    """Run curl command and output response"""
    _, stdout, _ = ssh_client.exec_command('curl http://127.0.0.1:5000/api/v1/')
    while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
        time.sleep(1)
    response = stdout.readlines()
    return response


def upload_from_local_to_remote(sftp_client):
    try:
        sftp_client.put(upload_local_path, upload_remote_path)
        print(f'Uploaded {upload_local_path} to remote {HOST}: {upload_remote_path}\n')
    except FileNotFoundError as e:
        print(f'Cannot upload from local machine to remote {HOST}...', e)


def download_from_remote_to_local(sftp_client):
    try:
        sftp_client.get(download_remote_path, download_local_path)
        print(f'Downloaded from remote {HOST}: {download_remote_path} to local {download_local_path}')
    except FileNotFoundError as e:
        print(f'Cannot download from remote {HOST} to local...\n', e)


def close_ssh_client(ssh_client):
    ssh_client.close()
    print('\nSSH client was closed.')


def close_sftp_client(sftp_client):
    sftp_client.close()
    print('\nSFTP client was closed.')


if __name__ == '__main__':
    # Connect to VM: returns ssh client
    ssh_session = connect_to_remote_host(HOST, USERNAME, PASSWORD)

    api_version_response = run_curl_command(ssh_session)

    for row in api_version_response:
        print(row)

    close_ssh_client(ssh_session)
