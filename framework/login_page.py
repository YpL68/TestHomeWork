from time import sleep
from framework.page import Page, WebDriver


class LoginPage(Page):
    title_login_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]'

    email_field_xpath: str = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'
    password_field_xpath: str = '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'
    login_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[4]'
    back_button_xpath: str = '//*[@resource-id="com.ajaxsystems:id/back"]'
    forgot_button_xpath: str = '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[3]'

    hamburger_menu_xpath: str = '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def user_login_emulation(self, email_str: str, password_str: str) -> bool:
        self.find_and_click_element(self.title_login_button_xpath)
        self.find_and_send_keys_element(self.email_field_xpath, email_str)
        self.find_and_send_keys_element(self.password_field_xpath, password_str)
        self.find_and_click_element(self.login_button_xpath)
        sleep(10)
        return True if self.find_element(self.hamburger_menu_xpath) else False


