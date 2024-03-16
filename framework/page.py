from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class Page:
    def __init__(self, driver: WebDriver, name_page: str):
        self.driver = driver
        self.name_page = name_page

    def find_element(self, xpath: str) -> WebElement | None:
        try:
            result = self.driver.find_element(AppiumBy.XPATH, xpath)
        except Exception:
            result = None
        return result

    def find_and_click_element(self, xpath: str) -> bool:
        try:
            self.find_element(xpath).click()
            return True
        except Exception:
            return False

    def find_and_send_keys_element(self, xpath: str, value: str) -> bool:
        try:
            self.find_element(xpath).send_keys(value)
            return True
        except Exception:
            return False
