import requests
from data import Url


class AuthMethods:
    def login(self, body):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_URL}', json=body)
        return response
