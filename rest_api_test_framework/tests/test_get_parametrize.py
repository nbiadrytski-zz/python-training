from rest_api_test_framework.utils.http_utils.response import ResponseValidator
from rest_api_test_framework.utils.http_utils.requests import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, title


@pytest.mark.package
@title('/api/version response contains "{value}"')
@description('Check that response contains expected values.')
@severity(severity_level.TRIVIAL)
@pytest.mark.parametrize('value', ['The', 'current', 'version', 'is', '2.0'])
def test_parametrize_contains_value(current_host, value):

    with step('Perform /api/version request'):
        actual_resp = GetRequest(current_host.host, path='/api/version').call()
        validator = ResponseValidator(actual_resp)

    with step('Response contains value.'):
        assert value in validator.contains(actual_resp)


@pytest.mark.package
@title('/api/version and api/status code is 200')
@description('Check status code is 200 for /api/version and /api/status endpoints.')
@severity(severity_level.NORMAL)
@pytest.mark.parametrize('path', ['/api/version', '/api/status'], ids=['version', 'status'])
def test_parametrize_status_code(current_host, path):

    with step('Perform GET request'):
        actual_resp = GetRequest(current_host.host, path).call()
        validator = ResponseValidator(actual_resp)

    with step('Status code is 200'):
        assert validator.get_status_code(actual_resp) == 200


@pytest.mark.package
@title('/api/version response does not contain values')
@description('Check that response does not contain provided strings.')
@severity(severity_level.MINOR)
@pytest.mark.parametrize('value', ['No', 'such', 'values', 'in', 'response'])
def test_parametrize_not_contains_value(current_host, value):

    with step('Perform /api/version request'):
        actual_resp = GetRequest(current_host.host, path='/api/version').call()
        validator = ResponseValidator(actual_resp)

    with step('Response does not contain provided string.'):
        assert value not in validator.contains(actual_resp)
