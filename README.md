# Sprint_6
# Проект автоматизации тестирования сайта заказа самокатов

1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install pytest, pip install selenium, pip install allure-pytest, установить драйвера для мозиллы
3. Команда для запуска — pytest -v .\test

Тесты:
1. test_main_page - файл с тестами главной страницы
   2. test_check_questions_and_answers - тест проверки вопросов и соответствия ответов
3. test_order_page - файл с тестами заказа
   4. test_create_order_order_button_header_success - тест проверки создания заказа через кнопку "Заказать" в заголовке страницы
   5. test_create_order_order_button_down_success - тест проверки создания заказа через кнопку "Заказать" в конце страницы
6. test_header_page - файл с тестами переходов по ссылке
   7. test_click_logo_scooter_follow_link_main - тест перехода по логотипу скутера на главную
   8. test_click_logo_ya_redirect_dzen - тест перехода по логотипу Яндекса на страницу Дзена

Папка allure_results содержит отчет по прогону тестов
