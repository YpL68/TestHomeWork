from framework.page import Page, WebDriver
from utils.android_utils import WebElementCheckException


class LoginPage(Page):
    email_field_xpath: str = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    password_field_xpath: str = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    login_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[4]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def fill_email_field(self, email_str: str):
        if not self.find_and_send_keys_element(self.email_field_xpath, email_str):
            raise WebElementCheckException(f"{self.name_page}: email field check error")

    def fill_password_field(self, password_str: str):
        if not self.find_and_send_keys_element(self.password_field_xpath, password_str):
            raise WebElementCheckException(f"{self.name_page}: password field check error")

    def login_button_click(self):
        if not self.find_and_click_element(self.login_button_xpath):
            raise WebElementCheckException(f"{self.name_page}: login button check error")
