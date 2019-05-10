from pytest import fixture
from api_framework.hosts_config import HostsConfig


def pytest_addoption(parser):
    parser.addoption('--env', action='store', help='Env to run tests against')


@fixture(scope='session')
def env(request):  # request (pytest built-in) keeps all command-line session info
    return request.config.getoption('--env')


@fixture(scope='session')
def current_host(env):
    cfg = HostsConfig(env)
    return cfg
