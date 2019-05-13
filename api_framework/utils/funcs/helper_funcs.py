from urllib import parse
from jsonpath_rw import parse as json_parser
import os
import dictdiffer
import logging
import json


logger = logging.getLogger(__name__)


def extract_path(url):
    """Extract path + query params from passed url"""
    path = parse.urlparse(url).path
    query = parse.urlparse(url).query
    return path + '?' + query


def find_item_by_jsonpath(actual_json, json_path, idx=0):
    """
    Get JSON item value by json_path using jsonpath_rw module.
    idx=0 by default (getting the 1st item from resulting list)
    """
    value = [match.value for match in json_parser(json_path).find(actual_json)][idx]
    return value


def file_content(file_path):
    """Return file content with provided file path"""
    file_path = os.getcwd() + file_path
    with open(file_path) as f:
        content = f.read()
    return content


def compare_dicts(actual_dict, expected_dict, ignore_keys):
    """
    Compare 2 dicts are equal.
    Pass the keys to be ignored to ignore_keys param.
    """
    difference = list(dictdiffer.diff(actual_dict, expected_dict, ignore=ignore_keys))
    if not difference:
        return True
    else:
        logger.info(f'Responses do not match:\n {difference}')
        return False


def convert_json_to_dict(file_path):
    file_path = os.getcwd() + file_path
    with open(file_path) as f:
        data = json.load(f)
    return data
