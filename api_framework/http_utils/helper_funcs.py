from urllib import parse


def extract_path(url):
    path = parse.urlparse(url).path
    query = parse.urlparse(url).query
    return path + '?' + query

