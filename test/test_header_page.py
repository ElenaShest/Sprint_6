from pages.header_page import HeaderPage


class TestHeaderPage:

    def test_click_logo_scooter_follow_link_main(self, browser):
        header_page = HeaderPage(browser)
        header_page.click_to_order_button_header()
        header_page.click_to_logo_scooter()
        assert header_page.check_main_page()

    def test_click_logo_ya_redirect_dzen(self, browser):
        header_page = HeaderPage(browser)
        header_page.click_to_logo_ya()
        assert header_page.check_redirect_dzen()
