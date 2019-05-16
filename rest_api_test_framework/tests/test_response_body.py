from rest_api_test_framework.utils.http_utils.response import ResponseValidator
from rest_api_test_framework.utils.http_utils.requests import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, title


@pytest.mark.package
class TestResponseBody:

    PATH_TO_FILE = '/resources/testdata/responses/'

    @title('Check plain text response body')
    @description('Check plain text response body equals to expected.')
    @severity(severity_level.TRIVIAL)
    def test_text_response_body(self, current_host):

        path = '/api/version'

        with step('Perform /api/version request'):
            actual_resp = GetRequest(current_host.host, path).call()
            validator = ResponseValidator(actual_resp)

        with step('Compare text response body'):
            assert validator.response_equals(
                actual_resp,
                expected_response=TestResponseBody.PATH_TO_FILE + 'api_version.txt'), \
                'Content of api_version.txt must be equal to actual response.'

    @title('Check json response body (ignore "redis"')
    @description('Compare json response body. Ignore "redis" key.')
    @severity(severity_level.BLOCKER)
    def test_json_response_body_some_keys_ignored(self, current_host):

        path = '/api/status'

        with step('Perform api/status request'):
            api_version_resp = GetRequest(current_host.host, path).call()
            validator = ResponseValidator(api_version_resp)

        with step('Compare actual and expected json responses.'):
            responses_match = validator.json_response_equals(
                actual_response=api_version_resp,
                expected_response=TestResponseBody.PATH_TO_FILE + 'api_status.json',
                config_section_title='keys',
                ignore_keys=('redis',))

        assert responses_match
