from pytest_rest_api_frmw.utils.base_request import BaseRequest
from rest_api_test_framework.utils.http_utils import Response


class TestApi:

    def test_simple_package(self, current_host):

        host = current_host.host

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        headers = {'User-Agent': 'test'}

        query_params = {
            'key1': 'value1',
            'key2': 'value2'
        }

        request = BaseRequest(host, path)
        response = request.get_request(query_params, headers)

        status_code = Response.get_status_code(response)
        connection_header = Response.get_response_header(response, 'Connection')
        services_s3 = Response.get_value_from_json(response, 'content[0].chapters[0].beacons[0].method')

        assert status_code == 200
        assert connection_header == 'Keep-alive'
        assert services_s3 == 'get'

    def test_able_to_extract_from_package(self, current_host):
        host = current_host.host

        path = '/api/mgid:arc:video:central:b71fddb3-2857-4cc3-a56c-dc580c743b46/mica.json'

        request = BaseRequest(host, path)
        response = request.get_request()

        master_pl_url = Response.get_value_from_json(response, 'stitchedstream.source')
        master_pl_response = BaseRequest.extracted_get_request(master_pl_url)

        status_code = Response.get_status_code(master_pl_response)
        content_type = Response.get_response_header(master_pl_response, 'Content-Type')

        assert status_code == 200
        assert content_type == 'application/vnd.apple.mpegurl;charset=utf-8'


