import paramiko

HOST = '10.6.221.128'
USERNAME = 'pyauto'
PASSWORD = 'PythonMentoringBY2019'

upload_local_path = '/Users/mikalai_biadrytski/Desktop/in.txt'
upload_remote_path = '/home/pyauto/in.txt'
download_remote_path = '/home/pyauto/out.txt'
download_local_path = '/Users/mikalai_biadrytski/Desktop/out.txt'

with paramiko.SSHClient() as ssh_client:
    ssh_client.load_system_host_keys()
    ssh_client.connect(HOST, username=USERNAME, password=PASSWORD)  # start centOS VM

    _, current_dir, _ = ssh_client.exec_command('pwd')
    _, stdout, _ = ssh_client.exec_command('ls')
    print(f'Directory {current_dir.read().decode("utf-8")[:-1]} contains:')
    for idx, line in enumerate(stdout):
        print(f'{idx}. {line}')

    with ssh_client.open_sftp() as sftp_client:

        try:
            # upload from local to remote
            sftp_client.put(upload_local_path, upload_remote_path)
            print(f'Uploaded {upload_local_path} to remote {HOST}: {upload_remote_path}\n')
        except FileNotFoundError as e:
            print(f'Cannot upload from local machine to remote {HOST}...', e)

        try:
            # download from remote to local
            sftp_client.get(download_remote_path, download_local_path)
            print(f'Downloaded from remote {HOST}: {download_remote_path} to local {download_local_path}')
        except FileNotFoundError as e:
            print(f'Cannot download from remote {HOST} to local...\n', e)
