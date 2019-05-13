from api_framework.utils.http_utils.base_url import BaseUrl
import requests


class GetRequest(BaseUrl):
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, query_params=None, headers=None):
        resp = requests.get(self.base_url,
                            verify=False,
                            params=query_params,
                            headers=headers)
        self.logger.info(f'GET REQUEST: {self.base_url}\n'
                         f'GET REQUEST PARAMS: {query_params}\n'
                         f'GET REQUEST HEADERS: {headers}\n')
        return resp
