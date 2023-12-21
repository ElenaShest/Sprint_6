from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTION_ITEM = [By.ID, "accordion__heading-{}"] # пункт вопроса
    ANSWER_ITEM = [By.ID, "accordion__panel-{}"] # пункт ответа
    IMPORTANT_QUESTION = [By.XPATH, ".//div[text()='Вопросы о важном']"] # блок с вопросами
    ORDER_BUTTON_DOWN = [By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']"] # Кнопка "Заказать" в конце страницы
    HEADER_ON_MAIN = [By.XPATH, ".//div[contains(@class, 'Home_Header')]"] # заголовок на главной
