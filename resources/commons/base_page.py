from appium.webdriver.webdriver import WebDriver

from resources.commons.driver import Driver


class BasePage:

    @property
    def __driver(self) -> WebDriver:
        return Driver.get_driver()

    def _click_element(self, locator):
        self.__driver.find_element(locator[0], locator[1]).click()
        print("Clicou no elemento!!!")
