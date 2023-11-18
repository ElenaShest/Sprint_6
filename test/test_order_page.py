from pages.order_page import OrderPage

from data import Data
data = Data()

def test_create_order_order_button_header_success(browser):
    OrderPage(browser).click_to_order_button_header()
    OrderPage(browser).click_to_cookie_button()
    OrderPage(browser).create_order(data.NAME, data.LASTNAME, data.ADDRESS, data.PHONE, data.DATE, data.COMMENT)
    assert OrderPage(browser).check_order_page()
    OrderPage(browser).click_to_logo_scooter()
    assert OrderPage(browser).check_main_page()

def test_create_order_order_button_down_success(browser):
    OrderPage(browser).click_to_cookie_button()
    OrderPage(browser).scroll_to_order_button_down()
    OrderPage(browser).click_to_order_button_down()
    OrderPage(browser).create_order(data.NAME, data.LASTNAME, data.ADDRESS, data.PHONE, data.DATE, data.COMMENT)
    assert OrderPage(browser).check_order_page()
    OrderPage(browser).click_to_logo_ya()
    assert OrderPage(browser).check_redirect_dzen()
