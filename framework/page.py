from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement

import framework.conf.logger

logger = framework.conf.logger.get_logger(__name__)


class Page:
    def __init__(self, driver: WebDriver, name_page: str):
        self.driver = driver
        self.name_page = name_page

    def find_element(self, element: dict, logging: bool = True) -> WebElement:
        try:
            element_id = element.get("id", None)
            if element_id is not None:
                return self.driver.find_element(AppiumBy.ID, element_id)
            else:
                return self.driver.find_element(AppiumBy.XPATH, element.get("xpath"))
        except Exception as err:
            if logging:
                logger.error(f"\nAn error occurred when searching for an element "
                             f"\"{element.get('name')}\"")
            raise err

    def find_and_click_element(self, element: dict, logging: bool = True):
        try:
            self.find_element(element).click()
        except Exception as err:
            if logging:
                logger.error(f"\nAn error occurred when clicking on an element "
                             f"\"{element.get('name')}\"")
            raise err

    def find_and_send_keys_element(self, element: dict, value: str, logging: bool = True):
        try:
            self.find_element(element).clear().send_keys(value)
        except Exception as err:
            if logging:
                logger.error(f"\nAn error occurred when sending keys to an element "
                             f"\"{element.get('name')}\"")
            raise err

    def find_key_element(self, element: dict) -> bool:
        try:
            self.find_element(element, False)
            return True
        except Exception:
            return False
