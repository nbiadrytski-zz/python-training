import uuid
import requests

content_path = "http://posting.mongo-arc-v2.mtvnservices.com/uca/v2/content/authoring/"
links_count = 0

with open('test.txt') as f:
    for line in f:
        links_count += line.count("xml")


def generate_uuid():
    new_uuid = uuid.uuid4()
    return new_uuid


for item in range(links_count):
    url = content_path + str(generate_uuid()) + ".xml"
    response = requests.get(url)
    if "There is no Content Record found under the Content Environment with ID" in response.text:
        print(url)
    else:
        print("UUID is not vacant: " + url)


# first run content_creation.py to get test.txt