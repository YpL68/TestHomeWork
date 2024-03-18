from framework.page import Page, WebDriver
from framework.login_page_elements import LoginPageElements as LPElements
from framework.hamburger_menu_elements import HamburgerMenuElements as HMElements
import framework.conf.logger

logger = framework.conf.logger.get_logger(__name__)


class LoginPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def user_login_emulation(self, email_str: str, password_str: str) -> None:
        self.driver.implicitly_wait(5)
        self.find_and_click_element(LPElements.title_login_button)
        self.find_and_send_keys_element(LPElements.email_field, email_str)
        self.find_and_send_keys_element(LPElements.password_field, password_str)
        self.find_and_click_element(LPElements.login_button)

    def user_login_test(self, email_str: str, password_str: str, expected: bool) -> bool | None:
        try:
            self.user_login_emulation(email_str, password_str)

            # for very long authorization on the emulator
            timeout = 20 if expected else 5
            self.driver.implicitly_wait(timeout)
            # -------------------------------------------------

            return True if self.find_key_element(HMElements.hamburger_menu_button) else False
        except Exception as err:
            logger.error(f"\nAn error occurred when user_login_test was called:\n{str(err)}")
            return None
