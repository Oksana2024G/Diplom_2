## Дипломный проект. Задание 2: Автотесты API

### Студент: Оксана Гордеева 
### Когорта: 13
### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers


### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов с формированием отчётов allure**

>  `pytest --alluredir=allure_results`

| Название файла           | Содержание файла                            |
|--------------------------|---------------------------------------------|
| Tests dir                | Директория с тестами                        |
| test_create_user.py      | Тесты на создание пользователя              |
| test_change_user_data.py | Тесты на изменение данных пользователя      |
| test_login.py            | Тесты на логин пользоваетля                 |
| test_create_order.py     | Тетсы на создание заказа                    |
| test_get_user_orders.py  | Тесты на получение списка заказов           | 
| conftest.py              | Фикстуры                                    |
| helpers.py               | Хэлпер для тела запросов                    |
| data.py                  | Файл с URL, body запросов и текстами ошибок |
| auth_methods.py          | http клиент к auth методам                  |
| user_methods.py          | http клиент к user методам                  |
| order_methods.py         | http клиент к order методам                 |
| generators.py            | Генератор данных                            |
| requirements.txt         | Файл с зависимостями                        |
| allure_results.dir       | Папка с отчетами Allure                     |
