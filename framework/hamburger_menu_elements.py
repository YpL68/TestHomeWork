from framework.page_element import PageElement


class HamburgerMenuElements:
    hamburger_menu_button = PageElement({
        "name": "hamburger menu button",
        "id": "com.ajaxsystems:id/menuDrawer",
        "xpath": '(//*[@resource-id="com.ajaxsystems:id/compose_view"])[1]'})
    app_settings = PageElement({
        "name": "app settings",
        "id": "com.ajaxsystems:id/settings",
        "xpath": '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]'})
    help = PageElement({
        "name": "help",
        "id": "com.ajaxsystems:id/help",
        "xpath": '//android.view.View[@resource-id="com.ajaxsystems:id/help"]'})
    report_log = PageElement({
        "name": "report_log",
        "id": "com.ajaxsystems:id/logs",
        "xpath": '//android.view.View[@resource-id="com.ajaxsystems:id/addSpace"]'})
    terms = PageElement({
        "name": "terms",
        "id": "com.ajaxsystems:id/documentation_text",
        "xpath": '//*[@resource-id="com.ajaxsystems:id/compose_menu"]/android.view.View/android.view.'
                 'View/android.widget.ScrollView[3]'})
    back_button = PageElement({
        "name": "back button",
        "id": "com.ajaxsystems:id/back",
        "xpath": '//*[@resource-id="com.ajaxsystems:id/back"]'})
    sign_out = PageElement({
        "name": "sign_out",
        "xpath": '(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/'
                 'android.view.View/android.view.View[1]'})
