import requests
import logging


class BaseRequest:
    LOGGER = logging.getLogger(__name__)

    def __init__(self, host, path):
        self.host = host
        self.path = path
        self.base_url = self.host + self.path

    def get_request(self, query_params=None, headers=None):
        resp = requests.get(self.base_url, verify=False, params=query_params, headers=headers)
        BaseRequest.LOGGER.info(f'Request: {self.base_url}\n'
                                f'Request params: {query_params}\n'
                                f'Request headers: {headers}\n')
        return resp

    @staticmethod
    def extracted_get_request(url, query_params=None, headers=None):
        resp = requests.get(url, verify=False, params=query_params, headers=headers)
        BaseRequest.LOGGER.info(f'Extracted request url: {url}\n'
                                f'Request headers: {headers}\n')
        return resp

