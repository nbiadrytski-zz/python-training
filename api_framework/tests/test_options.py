from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.options_request import OptionsRequest
from api_framework.utils.http_utils.requests.get_request import GetRequest
import pytest
from allure_commons._allure import step
from allure import description, severity


@pytest.mark.package
class TestOptionsRequests:

    @description('Verify that OPTIONS request can be performed.')
    @severity('MAJOR')
    def test_options_request(self, current_host):
        path = '/api/mgid:arc:video:central:ed840685-e3ed-42db-b2cc-d90c315828c9/mica.json'

        headers = {'User-Agent': 'test',
                   'Accept': '*/*',
                   'Access-control-request-method': 'GET',
                   'Access-control-request-headers': 'Content-type',
                   'Origin': 'www.cmt.com'}

        actual_response = OptionsRequest(current_host.host, path).call(headers=headers)
        validator = ResponseValidator(actual_response)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_response) == 200

        with step('Response header Access-Control-Allow-Origin: *'):
            assert validator.get_response_header(actual_response, 'Access-Control-Allow-Origin') == '*'
        with step('Response header Access-Control-Allow-Methods: GET,POST,DELETE,PUT'):
            assert validator.get_response_header(actual_response, 'Access-Control-Allow-Methods') == 'GET,POST,DELETE,PUT'

    @description('Verify GET request in OPTIONS class.')
    @severity('CRITICAL')
    def test_options_request_in_get_class(self, current_host):

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        actual_response = GetRequest(current_host.host, path).call()
        validator = ResponseValidator(actual_response)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_response) == 200


