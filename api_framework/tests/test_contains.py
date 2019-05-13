from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.get_request import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity


@pytest.mark.package
@description('Compare text response body.')
@severity('MAJOR')
def test_contains_value(current_host):

    path = '/api/version'

    actual_response = GetRequest(current_host.host, path).call()
    validator = ResponseValidator(actual_response)

    expected_value = 'The current version'

    with step('Response contains value'):
        assert expected_value in validator.contains(actual_response)
