from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.get_request import GetRequest
from api_framework.utils.funcs.helper_funcs import extract_path
import pytest
from allure_commons._allure import step
from allure import description, severity
# -m package --alluredir reports --env=dev -nauto


@pytest.mark.package
class TestGetRequests:

    def test_package_with_headers_and_params(self, current_host):
        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        headers = {'User-Agent': 'test'}

        query_params = {
            'key1': 'value1',
            'key2': 'value2'
        }

        actual_response = GetRequest(current_host.host, path).call(query_params=query_params, headers=headers)
        validator = ResponseValidator(actual_response)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_response) == 200, 'Status Code must be 200'

        with step('Response header Connection: keep-alive'):
            assert validator.get_response_header(actual_response, 'Connection') == 'keep-alive'

        with step('Beacon method is get'):
            assert validator.get_value_from_json(actual_response, 'content[0].chapters[0].beacons[0].method') == 'get'

    def test_package_without_headers_and_params(self, current_host):

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        actual_response = GetRequest(current_host.host, path).call()
        validator = ResponseValidator(actual_response)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_response) == 200

    @description('Verify that Master Playlist url can be extracted and called.')
    @severity('TRIVIAL')
    def test_extraction_from_package(self, current_host):

        with step('Package Request'):
            path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

            package_response = GetRequest(current_host.host, path).call()
            # extract MasterPlaylist from package response
            master_pl =\
                ResponseValidator(package_response).get_value_from_json(package_response, 'stitchedstream.source')

        with step('Master Playlist Request'):
            master_pl_response = GetRequest(current_host.host, extract_path(master_pl)).call()
            validator = ResponseValidator(master_pl_response)

        with step('Status code is 200'):
            assert validator.get_status_code(master_pl_response) == 200

        with step('Response header Content-Type: application/vnd.apple.mpegurl;charset=utf-8'):
            assert validator.get_response_header(master_pl_response,
                                                 'Content-Type') == 'application/vnd.apple.mpegurl;charset=utf-8'

        with step('Response header Vary: User-Agent'):
            assert validator.get_response_header(master_pl_response, 'Vary') == 'User-Agent'
