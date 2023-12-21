from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_TITLE_FIRST = [By.XPATH, ".//div[text()='Для кого самокат']"] # заголовок на первой странице заказа самоката
    FIELD_NAME = [By.XPATH, ".//input[@placeholder='* Имя']"] # поле ввода имени
    FIELD_LASTNAME = [By.XPATH, ".//input[@placeholder='* Фамилия']"] # поле ввода фамилии
    FIELD_ADDRESS = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"] # поле ввода адреса
    FIELD_METRO = [By.XPATH, ".//input[@placeholder='* Станция метро']"] # поле ввода метро
    CHOOSE_METRO = [By.XPATH, ".//li[@data-value={num}]"] # выпадающий список станций метро
    FIELD_PHONE = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"] # поле ввода номера телефона
    ONWARD_BUTTON = [By.XPATH, ".//button[text()='Далее']"] # кнопка "Далее"
    ORDER_TITLE_SECOND = [By.XPATH, ".//div[text()='Про аренду']"] # заголовок на второй странице заказа самоката
    FIELD_WHEN = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"] # поле ввода даты
    CHOOSE_DATE = (By.XPATH, ".//div[contains(@class, 'selected')]") # выбранная дата в календаре
    FIELD_LIMIT = [By.XPATH, ".//div[text()='* Срок аренды']"] # поле срока аренды
    CHOOSE_LIMIT = [By.CLASS_NAME, "Dropdown-option"] # варианты выпадающего списка срока аренды
    CHOOSE_SCOOTER = [By.XPATH, ".//label[contains(@class, 'Checkbox_Label')]"] # выбор самоката
    FIELD_COMMENT = [By.XPATH, ".//input[@placeholder='Комментарий для курьера']"] # поле ввода комментария для курьера
    ORDER_BUTTON = [By.XPATH, ".//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"] # кнопка "Заказать" под формой
    CONFIRM_WINDOW = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader')]"] # заголовок окна подтверждения заказа
    AGREE_BUTTON = [By.XPATH, ".//button[text()='Да']"] # кнопка "Да" при подтверждении заказа
    STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"] # кнопка "Посмотреть статус"
    CANCEL_BUTTON = [By.XPATH, ".//button[text()='Отменить заказ']"] # кнопка "Отменить заказ" на странице заказа
