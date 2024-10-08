from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from resources.commons.driver import Driver


class BasePage:

    @property
    def __driver(self) -> WebDriver:
        return Driver.get_driver()

    def _click_element(self, locator):
        self.__driver.find_element(locator[0], locator[1]).click()
        print("Clicou no elemento!!!")

    def _wait_and_send_keys(self, locator, text):
        WebDriverWait(self.__driver, 5).until(expected_conditions.visibility_of_element_located(locator)).send_keys(text)
        print(f"Esperou e escreveu: {text}")