from pytest import mark


@mark.xfail(reason='Env was not QA')  # I expect this test to fail
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == 'https://mydqa-env.com'
    assert port == 80


def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    # possible action:
    # driver.get(base_url)
    assert base_url == 'https://mydev-env.com'
    assert port == 8080


@mark.skip(reason='not a staging env')
def test_environment_is_staging(app_config):
    base_url = app_config.base_url
    assert base_url == 'staging'
