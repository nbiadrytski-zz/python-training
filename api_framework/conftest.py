from pytest import fixture
from api_framework.hosts_config import HostsConfig


def pytest_addoption(parser):
    """ Adds command line option '--env' for running tests """
    parser.addoption('--env', action='store', help='Env to run tests against')


@fixture(scope='session')
def env(request):
    """ request (pytest built-in) keeps all command-line session info """
    return request.config.getoption('--env')


@fixture(scope='session')
def current_host(env):
    cfg = HostsConfig(env)
    return cfg


@fixture()
def print_smth():
    print('Hello!!! I am print_smth fixture. Printing before the test starts...')
    yield print('Hello!!! I am print_smth fixture. Printing in the middle of the test...')
    print('Hello!!! I am print_smth fixture. Printing after the test...')
