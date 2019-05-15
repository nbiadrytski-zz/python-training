from urllib import parse
from jsonpath_rw import parse as json_parser
import os
import dictdiffer
import logging
import json


logger = logging.getLogger(__name__)


def extract_path(url):
    """
    Extract path + query params from passed url.
    E.g. '/api/version?key1=ke1' will be extracted from http://test.com/api/version?key1=ke1

    Parameters:
        url (str): url string

    Returns:
        str: path + query params
    """
    path = parse.urlparse(url).path
    query = parse.urlparse(url).query
    return path + '?' + query


def find_item_by_jsonpath(actual_json, json_path, idx=0):
    """
    Get JSON key value by json_path using jsonpath_rw module.
    Default idx=0 to get the 1st item from resulting list.

    Parameters:
        actual_json (dict): json response
        json_path (str): path to key
        idx (int): 1st item from resulting list

    Returns:
        str: key value
    """
    value = [match.value for match in json_parser(json_path).find(actual_json)][idx]
    return value


def file_content(file_path):
    """
    Return file content based on provided file path.

    Parameters:
        file_path (str): relative path to file

    Returns:
        str: file content
    """
    file_path = os.getcwd() + file_path
    with open(file_path) as f:
        content = f.read()
    return content


def compare_dicts(actual_dict, expected_dict, ignore_keys):
    """
    Compare 2 dicts are equal using dictdiffer module.
    Pass the keys to be ignored to ignore_keys param.

    Parameters:
        actual_dict (dict): actual dictionary
        expected_dict (dict): expected dictionary
        ignore_keys (tuple): json keys to be ignored

    Returns:
        bool: if two dicts are equal
    """
    difference = list(dictdiffer.diff(actual_dict, expected_dict, ignore=ignore_keys))
    if not difference:
        return True
    else:
        logger.info(f'Responses do not match:\n {difference}')
        return False


def convert_json_to_dict(file_path):
    """
    Convert .json file content to dictionary

    Parameters:
         file_path (str): relative path to .json file

    Returns:
        dict: dictionary
    """
    file_path = os.getcwd() + file_path
    with open(file_path) as f:
        data = json.load(f)
    return data
