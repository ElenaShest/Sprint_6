from selenium.webdriver.common.by import By

class GeneralLocators:
    ORDER_BUTTON_HEADER = [By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"] # Кнопка "Заказать" в шапке
    LOGO_SCOOTER = [By.XPATH, ".//img[@alt='Scooter']"] # Логотип Самоката
    LOGO_YA = [By.XPATH, ".//img[@alt='Yandex']"] # Логотип Яндекса
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"] # кнопка принятия кук
    DZEN_HEADER = [By.ID, "dzen-header"] # заголовок на странице дзена
