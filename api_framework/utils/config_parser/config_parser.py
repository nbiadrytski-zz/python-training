import configparser


class DataConfigParser:
    def __init__(self, config_path):
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)

    def get_ignored_keys(self, title, keys):
        ignored_keys = []
        for key in keys:
            key = self.parser.get(title, key)
            ignored_keys.append(key)
        return tuple(ignored_keys)
