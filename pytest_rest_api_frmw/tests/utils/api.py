import configparser
import logging
from allure_commons._allure import step
from pytest_rest_api_frmw.tests.utils.http_manager import HttpManager
from pytest_rest_api_frmw.tests.utils.json_fixture import JSONFixture


class Api:
    LOGGER = logging.getLogger(__name__)
    parser = configparser.ConfigParser()
    parser.read('simple_config.ini')

    BASE_URL = parser.get('jira', 'url')
    CREATE_ISSUE = BASE_URL + '/rest/api/2/issue/'
    DELETE_ISSUE = BASE_URL + '/rest/api/2/issue/{0}/'

    @staticmethod
    def login():
        with step('Login'):
            url = Api.BASE_URL
            user_name = Api.parser.get('jira', 'username')
            password = Api.parser.get('jira', 'password')

            result = HttpManager.auth(url, user_name, password)
            Api.LOGGER.info('TEST: Login with {0}, {1} credentials'.format(user_name, password))
            assert 200 == result.status_code

    @staticmethod
    def create_issue(project_key):
        with step('Create issue'):
            result = HttpManager.post(Api.CREATE_ISSUE, JSONFixture.for_create_issue(project_key))
            Api.LOGGER.info('TEST: Create issue. Method: {0}, Data: {1}'.
                            format('POST', JSONFixture.for_create_issue(project_key)))
            # TODO with this line allure report isn't generated:
            #  allure.attach("Create issue", JSONFixture.for_create_issue(project_key), AttachmentType.TEXT)
            return result

    # @allure.step - will not work as expected. Returned value will be a link to memory
    @staticmethod
    def delete_issue(issue_id):
        with step('Delete issue by ID'):
            result = HttpManager.delete(Api.DELETE_ISSUE.format(issue_id))
            Api.LOGGER.info(
                'TEST: Delete issue. Method: {0}, URL : {1}'.format('DELETE', Api.DELETE_ISSUE.format(issue_id)))
            return result
