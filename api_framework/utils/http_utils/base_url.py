import logging
import urllib3


class BaseUrl:

    def __init__(self, host='', path=''):
        self.host = host
        self.path = path
        self.base_url = self.host + self.path
        self.logger = logging.getLogger(__name__)
        # Disable InsecureRequestWarning: Unverified HTTPS request is being made.
        # Adding certificate verification is strongly advised.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
