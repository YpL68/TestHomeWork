import subprocess


class WebElementCheckException(Exception):
    pass


def get_dev_id() -> str | None:
    # return first device id in list or None if list is empty
    try:
        execute_result = subprocess.check_output(["adb", "devices"]).decode("utf-8")
        dev_id = execute_result.replace("\r", "").replace("\t", "\n").split("\n")[1]
        return dev_id if dev_id else None
    except Exception:
        return None


def android_get_desired_capabilities():
    capabilities = {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '11',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '11bd127d',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }

    dev_id = get_dev_id()
    if dev_id:
        capabilities["appium:udid"] = dev_id

    return capabilities
