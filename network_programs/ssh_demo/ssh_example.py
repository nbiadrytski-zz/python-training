import paramiko


# malina: 10.6.178.12, pi / raspberry
# python training: 10.6.221.128, pyauto / PythonMentoringBY2019

HOST = '10.6.179.100'
USERNAME = 'pi'
PASSWORD = 'raspberry'

#upload_local_path = '/Users/mikalai_biadrytski/Documents/autotests/udemy_python/python-training/network_programs/ssh_demo/gap_counter2.py'
#upload_remote_path = '/home/pi/gap_counter2.py'
download_remote_path = '/home/pi/git_projects/tsif-motor-library/results.csv'
download_local_path = '/Users/mikalai_biadrytski/Documents/results.csv'

with paramiko.SSHClient() as ssh_client:
    ssh_client.load_system_host_keys()
    ssh_client.connect(HOST, username=USERNAME, password=PASSWORD)  # start centOS VM

    # _, current_dir, _ = ssh_client.exec_command('pwd')
    # _, stdout, _ = ssh_client.exec_command('ls')
    # print(f'Directory {current_dir.read().decode("utf-8")[:-1]} contains:')
    # for idx, line in enumerate(stdout):
    #     print(f'{idx}. {line}')

    with ssh_client.open_sftp() as sftp_client:

        # try:
        #     # upload from local to remote
        #     sftp_client.put(upload_local_path, upload_remote_path)
        #     print(f'Uploaded {upload_local_path} to remote {HOST}: {upload_remote_path}\n')
        # except FileNotFoundError as e:
        #     print(f'Cannot upload from local machine to remote {HOST}...', e)

        try:
            # download from remote to local
            sftp_client.get(download_remote_path, download_local_path)
            print(f'Downloaded from remote {HOST}: {download_remote_path} to local {download_local_path}')
        except FileNotFoundError as e:
            print(f'Cannot download from remote {HOST} to local...\n', e)
