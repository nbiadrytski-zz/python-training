from rest_api_test_framework.utils.http_utils.response import ResponseValidator
from rest_api_test_framework.utils.http_utils.requests import PostRequest
from rest_api_test_framework.utils.funcs import convert_json_to_dict
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level, title


@pytest.mark.media
class TestPostParametrize:

    REQUEST_BODY = [
        '/resources/testdata/requests/api_submit1.json',
        '/resources/testdata/requests/api_submit2.json',
        '/resources/testdata/requests/api_submit3.json'
    ]

    IDS = ['1440x1080_resolution', '1280x720_resolution', '384x216_resolution']

    @title('POST transcoding request without url')
    @description('Post request: submit transcoding request without url')
    @severity(severity_level.NORMAL)
    @pytest.mark.parametrize('body', REQUEST_BODY, ids=IDS)
    def test_post_transcode_without_url_parametrized(self, current_host, body):

        path = '/api/submit'

        headers = {'Accept': 'application/seamless.app.resource-1.2+json',
                   'Content-Type': 'application/json'}

        with step('Perform POST transcoding request without url'):
            actual_resp = PostRequest(current_host.host, path).call(convert_json_to_dict(body), headers=headers)
            validator = ResponseValidator(actual_resp)

        with step('Status code is 400'):
            assert validator.get_status_code(actual_resp) == 400

        with step('Response Msg: Request does not contains url.'):
            assert validator.get_value_from_json(actual_resp, 'msg') == 'Request does not contains url.'
