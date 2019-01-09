import uuid

content_path = "http://posting.mongo-arc-v2.mtvnservices.com/uca/v2/content/authoring/"
count = 0

with open('test.txt') as f:
    for line in f:
        count += line.count("xml")


def generate_uuid():
    new_uuid = uuid.uuid4()
    return count * (content_path + str(new_uuid) + ".xml" + "\n")


print(generate_uuid())

# first run content\_creation.py