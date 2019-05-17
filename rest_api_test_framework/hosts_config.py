from rest_api_test_framework.utils.exceptions import UnsupportedEnvException


class HostsConfig:
    """
    List of supported environments (passed via command-line) matched to request's host.
    Raises custom UnsupportedEnvException if passed env is not supported or --env command line arg was missed.

    Parameters:
        env (str): environment
    """
    def __init__(self, env):
        supported_envs = ['dev',
                          'live',
                          'media']

        if env.lower() not in supported_envs:
            raise UnsupportedEnvException(env, supported_envs)

        self.host = {
            'live': 'https://seamless.mtvnservices.com',
            'dev': 'https://seamless-dev.mtvnservices.com',
            'media': 'http://seamless-media.mtvnservices.com'
        }[env]
