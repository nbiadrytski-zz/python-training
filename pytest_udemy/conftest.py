from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    print('I amm tearing down this browser')  # use -s option to see this printed
