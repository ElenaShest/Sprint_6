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

Папка allure_results содержит отчет по прогону тестов
