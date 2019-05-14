from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.get_request import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, title


@pytest.mark.package
@title('Parameterized test title: /api/version response contains "{value}"')
@pytest.mark.parametrize('value', ['The', 'current', 'version', 'is', '1.45'])
@description('Check that response contains expected values.')
@severity(severity_level.TRIVIAL)
def test_parametrize_contains_value(current_host, value):

    actual_response = GetRequest(current_host.host, path='/api/version').call()
    validator = ResponseValidator(actual_response)

    with step('Response contains value.'):
        assert value in validator.contains(actual_response)


@pytest.mark.package
@pytest.mark.parametrize('path', ['/api/version', '/api/status'], ids=['version', 'status'])
@description('Check status code 200 for /api/version and /api/status.')
@severity(severity_level.NORMAL)
def test_parametrize_status_code(current_host, path):

    actual_response = GetRequest(current_host.host, path).call()
    validator = ResponseValidator(actual_response)

    with step('Status code is 200'):
        assert validator.get_status_code(actual_response) == 200


@pytest.mark.package
@pytest.mark.parametrize('value', ['No', 'such', 'values', 'in', 'response'])
@description('Check that response does not contain provided strings.')
@severity(severity_level.MINOR)
def test_parametrize_not_contains_value(current_host, value):

    actual_response = GetRequest(current_host.host, path='/api/version').call()
    validator = ResponseValidator(actual_response)

    with step('Response does not contain provided string.'):
        assert value not in validator.contains(actual_response)
