from jsonpath_rw import parse
# https://github.com/kennknowles/python-jsonpath-rw
import logging


class ResponseValidator:

    def __init__(self, resp):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f'RESPONSE HEADERS: {resp.headers}')
        self.logger.info(f'STATUS CODE: {resp.status_code}')
        self.logger.info(f'RESPONSE BODY: {resp.text}')

    @staticmethod
    def get_status_code(resp):
        return resp.status_code

    @staticmethod
    def get_response_header(resp, header_name):
        return resp.headers[header_name]

    @staticmethod
    def get_value_from_json(resp, json_path, idx=0):
        """
        Get JSON item value by json_path using jsonpath_rw module.
        idx=0 by default (getting the 1st item from resulting list)
        """
        actual_json = resp.json()
        value = [match.value for match in parse(json_path).find(actual_json)][idx]
        return value