from jsonpath_rw import parse
# https://github.com/kennknowles/python-jsonpath-rw
import logging


class BaseResponse:
    LOGGER = logging.getLogger(__name__)

    @staticmethod
    def get_status_code(resp):
        status_code = resp.status_code
        BaseResponse.LOGGER.info(f'Status code: {status_code}\n')
        return resp.status_code

    @staticmethod
    def get_response_header(resp, header_name):
        resp_header = resp.headers[header_name]
        BaseResponse.LOGGER.info(f'Response headers: {resp.headers}\n')
        return resp_header

    @staticmethod
    def get_value_from_json(resp, json_path, idx=0):
        """
        Get JSON item value by json_path using jsonpath_rw module.
        idx=0 by default (getting the 1st item from resulting list)
        """
        actual_json = resp.json()
        BaseResponse.LOGGER.info(f'Response body: {actual_json}\n')
        value = [match.value for match in parse(json_path).find(actual_json)][idx]
        return value

