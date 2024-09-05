from appium.webdriver.common.appiumby import AppiumBy

from resources.commons.base_page import BasePage


class SettingsHome(BasePage):
    __BOTAO_SEARCH = (AppiumBy.ID, 'com.android.settings:id/search_action_bar')

    def __init__(self):
        super().__init__()

    def clicar_no_botao_de_procurar(self):
        self._click_element(SettingsHome.__BOTAO_SEARCH)
