import configparser
import os


class ConfigProvider:
    def __init__(self):
        self.config = configparser.ConfigParser()

        path_to_config = os.path.join(
            os.path.dirname(__file__), 'db.ini')
        self.config.read(path_to_config)

    def get(self, section, key):
        return self.config.get(section, key, fallback=None)

    def items(self, section):
        return self.config.items(section)

    def get_section_keys(self, section):
        return list(self.config[section])
