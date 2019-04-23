from pytest import fixture
from pytest_udemy_custom_configs.tests.config import Config


def pytest_addoption(parser):
    parser.addoption('--env', action='store', help='Env to run tests against')


@fixture(scope='session')
def env(request):  # request (pytest built-in) keeps all command-line session info
    return request.config.getoption('--env')


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg