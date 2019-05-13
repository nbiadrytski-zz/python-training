from api_framework.utils.http_utils.base_url import BaseUrl
import requests


class OptionsRequest(BaseUrl):
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, query_params=None, headers=None):
        resp = requests.options(self.base_url,
                                verify=False,
                                params=query_params,
                                headers=headers)

        self.logger.info(f'OPTIONS REQUEST: {self.base_url}\n'
                         f'OPTIONS REQUEST PARAMS: {query_params}\n'
                         f'OPTIONS REQUEST HEADERS: {headers}\n')
        return resp
