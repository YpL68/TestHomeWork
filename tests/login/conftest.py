import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def login_page_fixture(driver):
    yield LoginPage(driver)
