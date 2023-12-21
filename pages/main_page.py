import allure

from locators.general_locators import GeneralLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Кликнуть по кнопке 'да все привыкли'")
    def click_to_cookie_button(self):
        self.click_to_element(GeneralLocators.COOKIE_BUTTON)

    @allure.step("Проскроллить до блока 'Вопросы о важном'")
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.IMPORTANT_QUESTION)
        return self.find_definite_element(MainPageLocators.IMPORTANT_QUESTION)

    @allure.step("Кликнуть по вопросу")
    def get_question(self, num):
        method, locator = MainPageLocators.QUESTION_ITEM
        locator = locator.format(num)
        self.click_to_element((method, locator))
        return self.find_definite_element((method, locator))

    @allure.step("Сравнить тексты ответов")
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_ITEM
        locator = locator.format(num)
        return self.find_definite_element((method, locator)).text

