import configparser


class DataConfigParser:
    """
    Parses data from config .ini files.

    Parameters:
        config_path (str): relative path to config file.
    """
    def __init__(self, config_path):
        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)

    def get_ignored_keys(self, title, keys):
        """
        Get config key values based on provided config section title and keys

        Parameters:
            title (str): config section title
            keys (tuple): config keys

        Returns:
            tuple: keys to be ignored
        """
        ignored_keys = []
        for key in keys:
            key = self.parser.get(title, key)
            ignored_keys.append(key)
        return tuple(ignored_keys)
