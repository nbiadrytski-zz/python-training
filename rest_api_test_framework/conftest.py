from pytest import fixture
from rest_api_test_framework.hosts_config import HostsConfig
from rest_api_test_framework.utils.exceptions import NoEnvArgException


def pytest_addoption(parser):
    """Adds command line option '--env' for running tests"""
    parser.addoption('--env', action='store', help='Env to run tests against')


@fixture(scope='session')
def env(request):
    """
    pytest built-in request keeps all command line session info.
    Raises custom NoEnvArgException if --env command line arg was not passed.
    """
    if request.config.getoption('--env') is None:
        raise NoEnvArgException(request.config.getoption('--env'))
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
