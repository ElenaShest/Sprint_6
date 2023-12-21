import allure

from pages.header_page import HeaderPage


class TestHeaderPage:

    @allure.title("Клик по логотипу Самокат")
    @allure.description("Проверка, что клик по логотипу 'Самокат' переводит на главную страницу")
    def test_click_logo_scooter_follow_link_main(self, browser):
        header_page = HeaderPage(browser)
        header_page.click_to_order_button_header()
        header_page.click_to_logo_scooter()
        assert header_page.check_main_page()

    @allure.title("Клик по логотипу Яндекс")
    @allure.description("Проверка, что клик по логотипу 'Яндекс' редиректит на страницу Дзена (открывается новая вкладка)")
    def test_click_logo_ya_redirect_dzen(self, browser):
        header_page = HeaderPage(browser)
        header_page.click_to_logo_ya()
        assert header_page.check_redirect_dzen()
