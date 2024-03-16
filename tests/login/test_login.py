from time import sleep
from framework.login_page import LoginPage
from framework.home_page import HomePage


def test_find_battery(driver) -> None:
    driver.implicitly_wait(2)
    HomePage(driver).login_button_click()
    login_page = LoginPage(driver)
    login_page.fill_email_field("qa.ajax.app.automation@gmail.com")
    login_page.fill_password_field("qa_automation_password")
    login_page.login_button_click()
    sleep(15)