from api_framework.utils.http_utils.base_url import BaseUrl
from api_framework.utils.http_utils.base_request import BaseRequest
import requests


class OptionsRequest(BaseUrl, BaseRequest):
    """
    Inherits from BaseUrl and implements BaseRequest.
    Performs OPTIONS HTTP request using requests module.

    Parameters:
        host (str): request host.
        path (str): request api path.
    """
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, query_params=None, headers=None):
        """
        Performs OPTIONS HTTP request based on passed base_url, query params (optional), headers (optional).

        Parameters:
            query_params (dict): dictionary of OPTIONS request query params, e.g. {'key1': 'value1'}
            headers (dict): dictionary of OPTIONS request headers, e.g. {'User-Agent': 'test'}

        Returns:
            Response: Response object returned by HTTP request.
        """
        resp = requests.options(self.base_url,
                                verify=False,
                                params=query_params,
                                headers=headers)

        self.logger.info(f'OPTIONS REQUEST: {self.base_url}\n'
                         f'OPTIONS REQUEST PARAMS: {query_params}\n'
                         f'OPTIONS REQUEST HEADERS: {headers}\n')
        return resp
