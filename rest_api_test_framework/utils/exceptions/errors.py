class Error(Exception):
    """
    Base custom errors handling class. Formats error message.

    Parameters:
        message (str): error message
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class UnsupportedEnvException(Error):
    """
    Raised if invalid --env value or no value is passed as command line arg.

    Parameters:
        env (str): environment
        supported_envs (list): list of supported environments
    """

    def __init__(self, env, supported_envs):
        self.message = f'\n"{env}" is not a supported environment.\nSupported environments: {supported_envs}'


class NoEnvArgException(Error):
    """
    Raised if --env command line arg was not passed when starting tests.

    Parameters:
        env (str): environment
    """

    def __init__(self, env):
        self.message = f'\nCommand line arg "--env" is missing. Env is {env}'
