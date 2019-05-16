from rest_api_test_framework.utils.http_utils.response import ResponseValidator
from rest_api_test_framework.utils.http_utils.requests import GetRequest
from rest_api_test_framework.utils.funcs import extract_path
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, link, title


@pytest.mark.package
class TestGetRequests:

    PATH = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

    @title('Mica status code, Connection header, beacon method')
    @description('Check mica status code, Connection response header, beacon method')
    @severity(severity_level.CRITICAL)
    @link('https://docs.qameta.io/allure/#_links_5', name='More Info here')
    def test_mica_with_headers_and_params(self, current_host):

        params = {
            'key1': 'value1',
            'key2': 'value2'
        }

        headers = {'User-Agent': 'test'}

        with step('Perform mica.json request'):
            actual_resp = GetRequest(current_host.host, TestGetRequests.PATH).call(params, headers)
            validator = ResponseValidator(actual_resp)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_resp) == 200

        with step('Response header Connection: keep-alive'):
            assert validator.get_response_header(actual_resp, 'Connection') == 'keep-alive'

        with step('Beacon method is get'):
            assert validator.get_value_from_json(
                actual_resp, json_path='content[0].chapters[0].beacons[0].method') == 'get'

    @title('Mica status code')
    @description('Check mica.json status code')
    @severity(severity_level.BLOCKER)
    def test_mica_without_headers_and_params(self, current_host):

        with step('Perform mica.json request'):
            actual_resp = GetRequest(current_host.host, TestGetRequests.PATH).call()
            validator = ResponseValidator(actual_resp)

        with step('Status code is 200'):
            assert validator.get_status_code(actual_resp) == 200

    @title('Extract and call Master Playlist')
    @description('Check that Master Playlist url can be extracted form mica.json and called.')
    @severity(severity_level.NORMAL)
    def test_extraction_from_mica(self, current_host):

        with step('Perform mica.json equest'):
            mica_resp = GetRequest(current_host.host, TestGetRequests.PATH).call()
            # extract MasterPlaylist url from mica response
            pl = ResponseValidator(mica_resp).get_value_from_json(mica_resp, json_path='stitchedstream.source')

        with step('Perform Master Playlist request'):
            pl_resp = GetRequest(current_host.host, path=extract_path(pl)).call()
            validator = ResponseValidator(pl_resp)

        with step('Master Playlist response contains "#EXTM3U"'):
            assert '#EXTM3U' in validator.contains(pl_resp)

        with step('Status code is 200'):
            assert validator.get_status_code(pl_resp) == 200

        with step('Response header Content-Type: application/vnd.apple.mpegurl;charset=utf-8'):
            assert validator.get_response_header(pl_resp,
                                                 'Content-Type') == 'application/vnd.apple.mpegurl;charset=utf-8'

        with step('Response header Vary: User-Agent'):
            assert validator.get_response_header(pl_resp, 'Vary') == 'User-Agent'
