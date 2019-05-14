class HostsConfig:
    def __init__(self, env):

        supported_envs = ['dev',
                          'live',
                          'media']

        if env.lower() not in supported_envs:
            raise Exception(f'{env} is not a supported environment (supported envs: {supported_envs}')

        self.host = {
            'live': 'https://seamless.mtvnservices.com',
            'dev': 'https://seamless-dev.mtvnservices.com',
            'media': 'http://seamless-media.mtvnservices.com'
        }[env]
