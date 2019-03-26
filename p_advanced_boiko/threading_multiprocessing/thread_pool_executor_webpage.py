import requests
from concurrent.futures import ThreadPoolExecutor


download_list = [
    {'name': 'google', 'url': "http://google.com"},
    {'name': 'reddit', 'url': "http://reddit.com"},
    {'name': 'ebay', 'url': "http://ebay.com"},
    {'name': 'bbc', 'url': "http://bbc.co.uk"}
]


def download_page(page_info):
    r = requests.get(page_info['url'])
    with open(page_info['name'] + '.html', 'w') as save_file:
        save_file.writelines(r.text)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=10)

    # for item in download_list:
    #     pool.submit(download_page, item)

    pool.map(download_page, download_list)