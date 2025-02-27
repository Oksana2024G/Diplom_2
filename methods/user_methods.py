import allure
import requests
from curl import Url

class UserMethods:
    @staticmethod
    @allure.step("Регистрация")
    def register(body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER_URL}', json=body)
        return response

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token):
        headers = {
            "Authorization": f"{access_token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(f'{Url.BASE_URL}{Url.USER_URL}', headers=headers)
        return response

    @staticmethod
    @allure.step("Изменение данных пользователя")
    def change_user_data(access_token, user_data):
        headers = {
            "Authorization": f"{access_token}",
            "Content-Type": "application/json"
        }
        response = requests.patch(f'{Url.BASE_URL}{Url.USER_URL}', json=user_data, headers=headers)
        return response

    @staticmethod
    @allure.step("Изменение данных неавторизованного пользователя")
    def change_user_data_unauthorized(update_data):
        response = requests.patch(f'{Url.BASE_URL}{Url.USER_URL}', json=update_data)
        return response
