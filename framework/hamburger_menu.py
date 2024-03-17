from framework.page import Page, WebDriver
from framework.locators.hamburger_menu import LOCATORS as HML


class HamburgerMenu(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver, name_page="Login page")

    def hamburger_menu_element_click(self, element: dict) -> bool | None:
        try:
            self.driver.implicitly_wait(2)
            self.find_and_click_element(element)
            self.find_and_click_element(HML["back_button"])
            return True
        except Exception:
            return None

    def app_settings_click(self) -> bool | None:
        return self.hamburger_menu_element_click(HML["app_settings"])

    def help_click(self) -> bool | None:
        return self.hamburger_menu_element_click(HML["app_settings"])
