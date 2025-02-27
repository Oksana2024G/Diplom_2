import allure
import requests
from curl import Url

class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(ingredients, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = f"{access_token}"
        response = requests.post(f'{Url.BASE_URL}{Url.ORDERS_URL}', headers=headers, json=ingredients)
        return response

    @staticmethod
    @allure.step("Получение заказов пользователя")
    def get_user_orders(access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = f"{access_token}"
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_URL}', headers=headers)
        return response
