from api_framework.utils.http_utils.base_url import BaseUrl
from api_framework.utils.http_utils.base_request import BaseRequest
import requests
import json


class PostRequest(BaseUrl, BaseRequest):
    """
    Inherits from BaseUrl and implements BaseRequest.
    Performs POST HTTP request using requests module.

    Parameters:
        host (str): request host.
        path (str): request api path.
    """
    def __init__(self, host, path):
        super().__init__(host, path)

    def call(self, request_body, headers=None):
        """
        Performs POST HTTP request based on passed base_url, request body, headers (optional).

        Parameters:
            request_body (dict): .json file content converted to dictionary.
            headers (dict): dictionary of POST request headers, , e.g. {'User-Agent': 'test'}

        Returns:
            Response: Response object returned by HTTP request.
        """
        resp = requests.post(self.base_url,
                             data=json.dumps(request_body),
                             headers=headers)

        self.logger.info(f'POST REQUEST: {self.base_url}\n'
                         f'GET REQUEST BODY: {request_body}\n'
                         f'GET REQUEST HEADERS: {headers}\n')
        return resp
