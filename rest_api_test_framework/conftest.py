from pytest import fixture
from rest_api_test_framework.hosts_config import HostsConfig


def pytest_addoption(parser):
    """Adds command line option '--env' for running tests"""
    parser.addoption('--env', action='store', help='Env to run tests against')


@fixture(scope='session')
def env(request):
    """pytest built-in request keeps all command line session info"""
    return request.config.getoption('--env')


@fixture(scope='session')
def current_host(env):
    """
    Returns HostsConfig object based on passed env.
    Pass to each test method.

    Parameters:
        env (str): environment. See supported_envs in HostsConfig class

    Returns:
        HostsConfig: can be used to get host matched to passed env.
    """
    cfg = HostsConfig(env)
    return cfg
