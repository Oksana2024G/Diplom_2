import allure
import requests
from curl import Url


class AuthMethods:
    @staticmethod
    @allure.step("Авторизация пользователя")
    def login(body):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=body)
        return response
