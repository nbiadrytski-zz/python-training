from api_framework.http_utils.response_validator import ResponseValidator
from api_framework.http_utils.get_request import GetRequest
from api_framework.http_utils.helper_funcs import extract_path
import pytest
from allure_commons._allure import step
from allure import description, severity


@pytest.mark.package
class TestGetRequests:

    def test_package_with_headers_and_params(self, current_host):
        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        headers = {'User-Agent': 'test'}

        query_params = {
            'key1': 'value1',
            'key2': 'value2'
        }

        request = GetRequest(current_host.host, path).call(query_params=query_params, headers=headers)
        response = ResponseValidator(request)

        with step('Status code is 200'):
            assert response.get_status_code(request) == 200

        with step('Response header Connection: keep-alive'):
            assert response.get_response_header(request, 'Connection') == 'keep-alive'

        with step('Beacon method is get'):
            assert response.get_value_from_json(request, 'content[0].chapters[0].beacons[0].method') == 'get'

    def test_package_without_headers_and_params(self, current_host):

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        request = GetRequest(current_host.host, path).call()
        response = ResponseValidator(request)

        with step('Status code is 200'):
            assert response.get_status_code(request) == 200

    # @description('Verify that Master Playlist url can be extracted and called.')
    # @severity('TRIVIAL')
    # def test_extraction_from_package(self, current_host):
    #     with step('Package Request'):
    #         path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'
    #         package_response = GetRequest(current_host.host, path).call()
    #
    #
    #     with step('Master Playlist Request'):
    #         master_pl_url = Response.get_value_from_json(package_response, 'stitchedstream.source')
    #         master_pl_response = GetRequest.call_extracted_url(master_pl_url)
    #
    #         status_code = Response.get_status_code(master_pl_response)
    #         content_type = Response.get_response_header(master_pl_response, 'Content-Type')
    #
    #     with step('Status code is 200'):
    #         assert status_code == 200
    #     with step('Response header Content-Type: application/vnd.apple.mpegurl;charset=utf-8'):
    #         assert content_type == 'application/vnd.apple.mpegurl;charset=utf-8'

    @description('Verify that Master Playlist url can be extracted and called.')
    @severity('TRIVIAL')
    def test_extraction_from_package(self, current_host):
        with step('Package Request'):
            path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

            package_request = GetRequest(current_host.host, path).call()

            # extract MasterPlaylist from package response
            master_pl_url = ResponseValidator(package_request).get_value_from_json(package_request,
                                                                                   'stitchedstream.source')
        with step('Master Playlist Request'):

            master_pl_request = GetRequest(current_host.host, extract_path(master_pl_url)).call()
            master_pl_response = ResponseValidator(master_pl_request)

        with step('Status code is 200'):
            assert master_pl_response.get_status_code(master_pl_request) == 200

        with step('Response header Content-Type: application/vnd.apple.mpegurl;charset=utf-8'):
            assert master_pl_response.get_response_header(master_pl_request, 'Content-Type') == 'application/vnd.apple.mpegurl;charset=utf-8'

        with step('Response header Vary: User-Agent'):
            assert master_pl_response.get_response_header(master_pl_request, 'Vary') == 'User-Agent'
