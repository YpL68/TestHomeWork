from framework.page import Page, WebDriver
from utils.android_utils import WebElementCheckException


class HomePage(Page):
    login_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]'
    register_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[2]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Home page")

    def login_button_click(self):
        if not self.find_and_click_element(self.login_button_xpath):
            raise WebElementCheckException(f"{self.name_page}: login button check error")

    def register_button_click(self):
        if not self.find_and_click_element(self.register_button_xpath):
            raise WebElementCheckException(f"{self.name_page}: register button check error")
