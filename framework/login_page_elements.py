from framework.page_element import PageElement


class LoginPageElements:
    title_login_button = PageElement({
        "name": "title login button",
        "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]'})
    email_field = PageElement({
        "name": "email field",
        "xpath": '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginEmail"]'})
    password_field = PageElement({
        "name": "password field",
        "xpath": '//android.widget.EditText[@resource-id="com.ajaxsystems:id/authLoginPassword"]'})
    login_button = PageElement({
        "name": "login button",
        "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[4]'})
    forgot_button = PageElement({
        "name": "forgot button",
        "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[3]'})
    back_button = PageElement({
        "name": "back button",
        "id": "com.ajaxsystems:id/back",
        "xpath": '//*[@resource-id="com.ajaxsystems:id/back"]'})
