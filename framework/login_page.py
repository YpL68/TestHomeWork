from framework.page import Page, WebDriver


class LoginPage(Page):
    title_login_button: dict = \
        {"name": "title login button",
         "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]'}
    email_field: dict = \
        {"name": "email field",
         "xpath": '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'}
    password_field: dict = \
        {"name": "password field",
         "xpath": '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'}
    login_button: dict = \
        {"name": "login button",
         "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[4]'}
    back_button: dict = \
        {"name": "back button",
         "xpath": '//*[@resource-id="com.ajaxsystems:id/back"]'}
    forgot_button: dict = \
        {"name": "forgot button",
         "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[3]'}
    hamburger_menu_button: dict = \
        {"name": "hamburger menu button",
         "xpath": '//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'}

    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def user_login_emulation(self, email_str: str, password_str: str) -> bool | None:
        try:
            self.driver.implicitly_wait(30)  # emulator is very slow
            self.find_and_click_element(self.title_login_button)
            self.driver.implicitly_wait(5)
            self.find_and_send_keys_element(self.email_field, email_str)
            self.find_and_send_keys_element(self.password_field, password_str)
            self.find_and_click_element(self.login_button)

            return True if self.find_key_element(self.hamburger_menu_button) else False
        except Exception:
            return None
