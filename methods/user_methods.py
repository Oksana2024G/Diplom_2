import requests
from data import Url

class UserMethods:
    def register(self, body):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER_URL}', json=body)
        return response

    def delete_user(self, access_token):
        headers = {
            "Authorization": f"{access_token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(f'{Url.BASE_URL}{Url.USER_URL}', headers=headers)
        return response

    def change_user_data(self, access_token, user_data):
        headers = {
            "Authorization": f"{access_token}",
            "Content-Type": "application/json"
        }
        response = requests.patch(f'{Url.BASE_URL}{Url.USER_URL}', json=user_data, headers=headers)
        return response

    def change_user_data_unauthorized(self, update_data):
        response = requests.patch(f'{Url.BASE_URL}{Url.USER_URL}', json=update_data)
        return response
