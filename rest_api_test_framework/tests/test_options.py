from rest_api_test_framework.utils.http_utils.response import ResponseValidator
from rest_api_test_framework.utils.http_utils.requests import OptionsRequest, GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, title


@pytest.mark.package
class TestOptionsRequests:

    @title('OPTIONS request')
    @description('Check that OPTIONS request can be performed.')
    @severity(severity_level.NORMAL)
    def test_options_request(self, current_host):

        path = '/api/mgid:arc:video:central:ed840685-e3ed-42db-b2cc-d90c315828c9/mica.json'

        headers = {'User-Agent': 'test',
                   'Accept': '*/*',
                   'Access-control-request-method': 'GET',
                   'Access-control-request-headers': 'Content-type',
                   'Origin': 'www.cmt.com'}

        with step('Perform OPTIONS request'):
            actual_resp = OptionsRequest(current_host.host, path).call(headers=headers)
            validator = ResponseValidator(actual_resp)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_resp) == 200

        with step('Response header Access-Control-Allow-Origin: *'):
            assert validator.get_response_header(actual_resp, 'Access-Control-Allow-Origin') == '*'

        with step('Response header Access-Control-Allow-Methods: GET,POST,DELETE,PUT'):
            assert validator.get_response_header(actual_resp, 'Access-Control-Allow-Methods') == 'GET,POST,DELETE,PUT'

    @title('GET request in OPTIONS class')
    @description('Check GET request in OPTIONS class.')
    @severity(severity_level.TRIVIAL)
    def test_get_request_in_options_class(self, current_host):

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        with step('Perform GET request'):
            actual_resp = GetRequest(current_host.host, path).call()
            validator = ResponseValidator(actual_resp)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_resp) == 200
