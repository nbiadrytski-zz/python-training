import requests
import time
import threading


download_list = [
    {'name': 'google', 'url': "http://google.com"},
    {'name': 'reddit', 'url': "http://reddit.com"},
    {'name': 'ebay', 'url': "http://ebay.com"},
    {'name': 'bbc', 'url': "http://bbc.co.uk"}
]


def status_update():
    """Print 'Still downloading' at regular intervals."""
    while True:
        print("Still downloading...")
        time.sleep(0.1)


def download_page(page_info):
    """Download and save web page."""
    r = requests.get(page_info['url'])
    with open(page_info['name'] + '.html', 'w') as save_file:
        save_file.write(r.text)


if __name__ == '__main__':
    for download in download_list:
        downloader = threading.Thread(target=download_page, args=(download,))
        downloader.start()

    status = threading.Thread(target=status_update)
    status.daemon = True  # Python will exit when only daemon threads are left running.
    status.start()