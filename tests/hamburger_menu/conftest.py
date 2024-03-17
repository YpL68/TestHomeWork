import pytest

from framework.conf.constants import CORRECT_EMAIL, CORRECT_PASSWORD
from framework.hamburger_menu import HamburgerMenu
from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def login(driver):
    LoginPage(driver).user_login_test(CORRECT_EMAIL, CORRECT_PASSWORD)


@pytest.fixture(scope='function')
def hamburger_menu_fixture(driver):
    yield HamburgerMenu(driver)