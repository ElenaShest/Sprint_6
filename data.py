import random


class Urls:
    MAIN_URL = "https://qa-scooter.praktikum-services.ru/" # адрес главной
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order" # адрес заказа
    DZEN_URL = "https://dzen.ru/?yredirect=true" # адрес дзена

class Data:
    NAME_LIST = ["Вася", "Петя", "Оля", "Лена", "Света", "Коля"]
    NAME = random.choice(NAME_LIST)

    LASTNAME_LIST = ["Петров", "Иванов", "Смехова", "Смирнова", "Дубко", "Сидоров"]
    LASTNAME = random.choice(LASTNAME_LIST)

    ADDRESS_LIST = ["Екатеринбург, ул.Ленина, д.3а", "Москва, ул.Ленина, д.5", "Липецк, ул.Ленина, д.7"]
    ADDRESS = random.choice(ADDRESS_LIST)

    PHONE = f'+7{random.randint(9000000000, 9999999999)}'

    DATE_LIST = ["01.12.2023", "31.12.2023"]
    DATE = random.choice(DATE_LIST)

    COMMENT_LIST = ["Никаких комментариев, хорошего дня)", "Обязательно позвоните за день до заказа"]
    COMMENT = random.choice(COMMENT_LIST)
