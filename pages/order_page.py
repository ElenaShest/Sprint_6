import time
import random

import allure

from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Заказать' в заголовке")
    def click_to_order_button_header(self):
        self.click_to_element(GeneralLocators.ORDER_BUTTON_HEADER)

    @allure.step("Проскроллить до кнопки 'Заказать'")
    def scroll_to_order_button_down(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_DOWN)
        return self.find_definite_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Кликнуть по кнопке 'Заказать' внизу страницы")
    def click_to_order_button_down(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_DOWN)

    @allure.step("Кликнуть по кнопке 'да все привыкли'")
    def click_to_cookie_button(self):
        self.click_to_element(GeneralLocators.COOKIE_BUTTON)

    @allure.step("Заполнить поле 'Имя'")
    def set_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_NAME, text)

    @allure.step("Заполнить поле 'Фамилия'")
    def set_lastname_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_LASTNAME, text)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_ADDRESS, text)

    @allure.step("Кликнуть по полю 'Метро'")
    def click_to_metro(self):
        self.click_to_element(OrderPageLocators.FIELD_METRO)

    @allure.step("Выбрать станцию метро из выпадающего списка")
    def choose_metro_station(self):
        method, locator = OrderPageLocators.CHOOSE_METRO
        number = random.randint(1, 112)
        locator = locator.format(num=number)
        self.click_to_element((method, locator))

    @allure.step("Заполнить поле 'Телефон'")
    def set_phone_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_PHONE, text)

    @allure.step("Кликнуть по кнопке 'Далее'")
    def click_to_onward_button(self):
        self.click_to_element(OrderPageLocators.ONWARD_BUTTON)

    @allure.step("Заполнить поле 'Когда привезти самокат'")
    def set_date_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_WHEN, text)

    @allure.step("Кликнуть выбранную дату в календаре")
    def click_to_choose_date(self):
        self.click_to_element(OrderPageLocators.CHOOSE_DATE)

    @allure.step("Кликнуть по полю 'Срок аренды'")
    def click_to_rent_date(self):
        self.click_to_element(OrderPageLocators.FIELD_LIMIT)

    @allure.step("Выбрать вариант из выпадающего списка 'Срок аренды'")
    def choose_date(self):
        options = self.find_option_elements(OrderPageLocators.CHOOSE_LIMIT)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Выбрать любой самокат")
    def choose_scooter(self):
        options = self.find_option_elements(OrderPageLocators.CHOOSE_SCOOTER)
        random_option = random.choice(options)
        random_option.click()

    @allure.step("Добавить комментарий для курьера")
    def set_comment_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.FIELD_COMMENT, text)

    @allure.step("Кликнуть по кнопке заказа")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def click_to_confirm_button(self):
        self.click_to_element(OrderPageLocators.AGREE_BUTTON)

    @allure.step("Проверить, что заказ успешный")
    def check_success_order(self):
        return self.find_definite_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step("Кликнуть на кнопку 'Посмотреть статус'")
    def click_to_status_button(self):
        self.click_to_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step("Проверить, что перешли на страницу заказа")
    def check_order_page(self):
        return self.find_definite_element(OrderPageLocators.CANCEL_BUTTON)

    @allure.step("Кликнуть на логотип 'Самокат'")
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


    def create_order(self, name, lastname, address, phone, date, comment):
        self.set_name_to_field(name)
        self.set_lastname_to_field(lastname)
        self.set_address_to_field(address)
        self.click_to_metro()
        self.choose_metro_station()
        self.set_phone_to_field(phone)
        self.click_to_onward_button()
        self.set_date_to_field(date)
        self.click_to_choose_date()
        self.click_to_rent_date()
        self.choose_date()
        self.choose_scooter()
        self.set_comment_to_field(comment)
        self.click_to_order_button()
        self.click_to_confirm_button()
        self.check_success_order()
        self.click_to_status_button()
