import logging


class BaseUrl:

    def __init__(self, host='', path=''):
        self.host = host
        self.path = path
        self.base_url = self.host + self.path
        self.logger = logging.getLogger(__name__)
