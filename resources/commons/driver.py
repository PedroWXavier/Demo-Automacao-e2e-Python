from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.webdriver import WebDriver

from resources.appium.appium_config import appium_server_url, capabilities


class Driver:
    __driver: WebDriver = None

    @classmethod
    def get_driver(cls) -> WebDriver:
        if cls.__driver is None:
            cls.__driver = webdriver.Remote(command_executor=appium_server_url,
                                            options=UiAutomator2Options().load_capabilities(capabilities))
        return cls.__driver
