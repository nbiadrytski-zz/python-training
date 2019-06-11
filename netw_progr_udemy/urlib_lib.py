import urllib.request


headers = {}
headers['User-Agent'] = 'test'

req = urllib.request.Request('https://www.python.org', headers=headers)  # request object
html = urllib.request.urlopen(req).read()

print(html.decode())

print('\n\nDownloading Wordpress...')
rsp = urllib.request.urlopen('https://wordpress.org/latest.zip')
data = rsp.read()

filename = 'latest.zip'
file_ = open(filename, 'w')
file_.write(str(data))
file_.close()
print('Download complete...')