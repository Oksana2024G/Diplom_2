import allure
import pytest
import helper
import requests
from data import ErrorMessages
from generators import generate_user_body

class TestLoginCourier:
    @allure.title('Проверка успешной авторизации пользователя')
    def test_successful_user_login(self, create_user_and_get_token, auth_methods, user_methods):
        user_data, _ = create_user_and_get_token
        login_body = {"email": user_data["email"], "password": user_data["password"]}
        response = auth_methods.login(login_body)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "accessToken" in response.json()

    @allure.title('Проверка невозможности авторизации пользователя с неверными учетными данными')
    def test_impossibility_login_user_with_incorrect_credentials(self, create_user_and_get_token, auth_methods, user_methods):
        user_data = generate_user_body()
        login_body = {"email": user_data["email"], "password": user_data["password"]}
        response = auth_methods.login(login_body)
        assert response.status_code == 401
        assert response.json() == ErrorMessages.INCORRECT_LOGIN_MESSAGE
