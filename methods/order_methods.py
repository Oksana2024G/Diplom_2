import requests
from data import Url

class OrderMethods:
    def create_order(self, ingredients, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = f"{access_token}"
        response = requests.post(f'{Url.BASE_URL}{Url.ORDERS_URL}', headers=headers, json=ingredients)
        return response

    def get_user_orders(self, access_token=None):
        headers = {}
        if access_token:
            headers["Authorization"] = f"{access_token}"
        response = requests.get(f'{Url.BASE_URL}{Url.ORDERS_URL}', headers=headers)
        return response
