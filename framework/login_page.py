from framework.page import Page, WebDriver
from framework.locators.login_page import LOCATORS as LPL
from framework.locators.hamburger_menu import LOCATORS as HML


class LoginPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def user_login_emulation(self, email_str: str, password_str: str) -> None:
        self.driver.implicitly_wait(5)
        self.find_and_click_element(LPL["title_login_button"])
        self.find_and_send_keys_element(LPL["email_field"], email_str)
        self.find_and_send_keys_element(LPL["password_field"], password_str)
        self.find_and_click_element(LPL["login_button"])

    def user_login_test(self, email_str: str, password_str: str, expected: bool) -> bool | None:
        try:
            self.user_login_emulation(email_str, password_str)

            # for very long authorization on the emulator
            timeout = 20 if expected else 5
            self.driver.implicitly_wait(timeout)
            # -------------------------------------------------

            return True if self.find_key_element(HML["hamburger_menu_button"]) else False
        except Exception:
            return None
