import subprocess
import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.android_utils import android_get_desired_capabilities

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(android_get_desired_capabilities())


@pytest.fixture(scope="session")
def run_appium_server():
    subprocess.Popen(
        ["appium", "-a", "0.0.0.0", "-p", "4723", "--allow-insecure", "adb_shell"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope="function")
def driver(run_appium_server):
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    app_driver.implicitly_wait(10)
    yield app_driver
    if app_driver:
        app_driver.quit()
