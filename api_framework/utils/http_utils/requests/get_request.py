from api_framework.utils.http_utils.base_url import BaseUrl
from api_framework.utils.http_utils.base_request import BaseRequest
import requests


class GetRequest(BaseUrl, BaseRequest):
    """
    Inherits from BaseUrl and implements BaseRequest.
    Performs GET HTTP request using requests module.

    Parameters:
        host (str): request host.
        path (str): request api path.
    """
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, query_params=None, headers=None):
        """
        Performs GET HTTP request based on passed base_url, query params (optional), headers (optional).

        Parameters:
            query_params (dict): dictionary of GET request query params, e.g. {'User-Agent': 'test'}
            headers (dict): dictionary of GET request headers, e.g. {'key1': 'value1'}

        Returns:
            Response: Response object returned by HTTP request.
        """
        resp = requests.get(self.base_url,
                            verify=False,
                            params=query_params,
                            headers=headers)

        self.logger.info(f'GET REQUEST: {self.base_url}\n'
                         f'GET REQUEST PARAMS: {query_params}\n'
                         f'GET REQUEST HEADERS: {headers}\n')
        return resp
