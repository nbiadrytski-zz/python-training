from api_framework.utils.http_utils.response.response_validator import ResponseValidator
from api_framework.utils.http_utils.requests.post_request import PostRequest
from api_framework.utils.funcs.helper_funcs import convert_json_to_dict
import pytest
from allure_commons._allure import step
from allure import description, severity, severity_level


@pytest.mark.media
class TestPostParametrize:

    REQUEST_BODY = ['/resources/testdata/requests/api_submit1.json',
                    '/resources/testdata/requests/api_submit2.json',
                    '/resources/testdata/requests/api_submit3.json']

    IDS = ['1440x1080_resolution', '1280x720_resolution', '384x216_resolution']

    @pytest.mark.parametrize('body', REQUEST_BODY, ids=IDS)
    @description('Post request: submit transcoding request without url')
    @severity(severity_level.NORMAL)
    def test_post_transcode_without_url_parametrized(self, current_host, body):
        path = '/api/submit'

        headers = {'Accept': 'application/seamless.app.resource-1.2+json',
                   'Content-Type': 'application/json'}

        actual_response = PostRequest(current_host.host, path).call(convert_json_to_dict(body), headers)
        validator = ResponseValidator(actual_response)

        with step('Status code is 400'):
            assert validator.get_status_code(actual_response) == 400

        with step('Response Msg: Request does not contains url.'):
            assert validator.get_value_from_json(actual_response, 'msg') == 'Request does not contains url.'
