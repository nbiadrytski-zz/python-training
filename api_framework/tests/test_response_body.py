from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.get_request import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity


@pytest.mark.package
class TestResponseBody:

    @description('Compare text response body.')
    @severity('MAJOR')
    def test_text_response_body(self, current_host):
        path = '/api/version'

        actual_response = GetRequest(current_host.host, path).call()
        validator = ResponseValidator(actual_response)

        with step('Compare text response body'):
            assert validator.response_equals(actual_response,'/resources/testdata/responses/api_version.txt'), \
                'Content of api_version.txt is not equal to actual response'

    @description('Compare json response body (some keys ignored).')
    @severity('CRITICAL')
    def test_json_response_body_some_keys_ignored(self, current_host):
        path = '/api/status'

        with step('Perform api/status request'):
            api_version_response = GetRequest(current_host.host, path).call()
            validator = ResponseValidator(api_version_response)

        with step('Compare actual and expected json responses.'):
            responses_match = validator.json_response_equals(
                actual_response=api_version_response,
                expected_response='/resources/testdata/responses/api_status.json',
                config_section_title='keys',
                ignore_keys=('redis',))

        assert responses_match
