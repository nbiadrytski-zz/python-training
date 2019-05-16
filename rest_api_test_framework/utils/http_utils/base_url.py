import logging
import urllib3


class BaseUrl:
    """
    Builds base url based on provided request host and path.
    Creates logger object.
    Disables InsecureRequestWarning for unverified HTTPS requests.

    Parameters:
        host (str): request host.
        path (str): request api path.
    """

    def __init__(self, host='', path=''):
        self.host = host
        self.path = path
        self.base_url = self.host + self.path
        self.logger = logging.getLogger(__name__)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
