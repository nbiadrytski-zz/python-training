from api_framework.http_utils.response_validator import ResponseValidator
from api_framework.http_utils.options_request import OptionsRequest
from api_framework.http_utils.get_request import GetRequest
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

        request = OptionsRequest(current_host.host, path).call(headers=headers)
        response = ResponseValidator(request)

        with step('Status code is 200'):
            assert response.get_status_code(request) == 200

        with step('Response header Access-Control-Allow-Origin: *'):
            assert response.get_response_header(request, 'Access-Control-Allow-Origin') == '*'
        with step('Response header Access-Control-Allow-Methods: GET,POST,DELETE,PUT'):
            assert response.get_response_header(request, 'Access-Control-Allow-Methods') == 'GET,POST,DELETE,PUT'

    @description('Verify GET request in OPTIONS class.')
    @severity('CRITICAL')
    def test_options_request_in_get_class(self, current_host):

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        request = GetRequest(current_host.host, path).call()
        response = ResponseValidator(request)

        with step('Status code is 200'):
            assert response.get_status_code(request) == 200


