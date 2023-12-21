import allure

from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Заказать' в заголовке")
    def click_to_order_button_header(self):
        self.click_to_element(GeneralLocators.ORDER_BUTTON_HEADER)

    @allure.step("Кликнуть по логотипу 'Самокат'")
    def click_to_logo_scooter(self):
        self.click_to_element(GeneralLocators.LOGO_SCOOTER)

    @allure.step("Проверить, что перешли на главную страницу")
    def check_main_page(self):
        return self.find_definite_element(MainPageLocators.HEADER_ON_MAIN)

    @allure.step("Кликнуть по логотипу 'Яндекс'")
    def click_to_logo_ya(self):
        self.click_to_element(GeneralLocators.LOGO_YA)

    @allure.step("Проверить, что открылась новая вкладка Дзен")
    def check_redirect_dzen(self):
        self.redirect_new_tab()
        return self.find_definite_element(GeneralLocators.DZEN_HEADER)
