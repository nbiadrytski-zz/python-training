import xmltodict
import re
import requests
import os
import uuid

uuid_regexp = "[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}"
content_path = "http://posting.mongo-arc-v2.mtvnservices.com/uca/v2/content/authoring/"
media_episode_feed_url = '''http://feeds.mtvnservices.com/media/feed/media-episode-feed?ds.namespace=comedycentral.com&query.uuid=6af4c818-2394-11e9-b5e7-70df2f866ace&ds.stage=live&ds.nodp=false&lookupParentRating=true'''
feed_videos = []
video_files_response = []
separator = 112 * "="
color_start = "\033[1m"
color_end = "\033[0m"


def generate_uuid():
    new_uuid = uuid.uuid4()
    return str(new_uuid)


def store_response_in_xml(file_name, url):
    response = requests.get(url)
    with open(file_name, 'wb') as file:
        file.write(response.content)
    return file_name


def get_xml_response(file_name):
    with open(file_name) as f:
        doc = xmltodict.parse(f.read())
    return doc


def get_feed_videos(document):
    print(color_start + "Videos links:" + color_end)
    for x in document['metaMedia']['media']:
        ids_unsorted = re.findall(uuid_regexp, str(x))
        ids_set = set(ids_unsorted)
        ids_sorted = list(ids_set)
        for id in ids_sorted:
            feed_videos.append(id)
            print(content_path + id + ".xml")
    print(separator + "\n")
    return feed_videos


def get_videoassetrefs_links(document):
    for item in document['content-record']['link-list']:
        if "VideoAssetRefs" in str(item):
            ids_unsorted = re.findall(uuid_regexp, str(item))
            ids_set = set(ids_unsorted)
            ids_sorted = list(ids_set)
            for id in ids_sorted:
                print(content_path + id + ".xml")


def get_transcriptassetrefs_links(document):
    for item in document['content-record']['link-list']:
        if "TranscriptAssetRefs" in str(item):
            ids_unsorted = re.findall(uuid_regexp, str(item))
            ids_set = set(ids_unsorted)
            ids_sorted = list(ids_set)
            for id in ids_sorted:
                print(content_path + id + ".xml")
    print(separator + "\n")


# Print feed videos
xml = get_xml_response(store_response_in_xml("media-episode-feed.xml", media_episode_feed_url))
get_feed_videos(xml)

# Call videos and store responses in xml files like video.xml
for i in range(len(feed_videos)):
    store_response_in_xml("video" + str(i) + ".xml", content_path + feed_videos[i] + ".xml")

# Get all files from current directory
files_in_dir = [f for f in os.listdir('.') if os.path.isfile(f)]
# Filter current directory files by pattern "video.xml"
video_files = [s for s in files_in_dir if "video" in s]

# Print VideoAssetRefs and TranscriptAssetRefs for each video
for i in range(len(video_files)):
    video_files_response.append(get_xml_response(video_files[i]))
    print(color_start + "VideoAssetRefs for video" + str(i) + color_end)
    get_videoassetrefs_links(video_files_response[i])
    print(color_start + "TranscriptAssetRefs for video" + str(i) + color_end)
    get_transcriptassetrefs_links(video_files_response[i])


# to save console output to test.txt run:
# python3 content_creation.py > test.txt







