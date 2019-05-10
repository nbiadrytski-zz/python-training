from api_framework.http_utils.base_url import BaseUrl
import requests


class GetRequest(BaseUrl):
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, query_params=None, headers=None):
        resp = requests.get(self.base_url,
                            verify=False,
                            params=query_params,
                            headers=headers)
        self.logger.info(f'\n\nGET REQUEST: {self.base_url}\n'
                         f'GET REQUEST PARAMS: {query_params}\n'
                         f'GET REQUEST HEADERS: {headers}\n')
        return resp

    # @staticmethod
    # def call_extracted_url(url, query_params=None, headers=None):
    #     resp = requests.get(url,
    #                         verify=False,
    #                         params=query_params,
    #                         headers=headers)
    #     BaseUrl().logger.info(f'EXTRACTED REQUEST URL: {url}\n'
    #                           f'REQUEST HEADERS: {headers}\n')
    #     return resp
