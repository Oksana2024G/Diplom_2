import allure
import pytest
from data import ErrorMessages
from generators import generate_user_body
from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title('Проверка успешного создания нового пользователя')
    def test_success_created_user(self):
        user_data = generate_user_body()
        response = UserMethods.register(user_data)
        assert response.status_code == 200
        assert 'accessToken' in response.json()

    @allure.title('Проверка невозможности создания двух одинаковых пользователей')
    def test_impossibility_creating_two_same_users(self):
        user_data = generate_user_body()
        UserMethods.register(user_data)
        second_user = UserMethods.register(user_data)
        assert second_user.status_code == 403 and second_user.json() == ErrorMessages.LOGIN_ALREADY_USED_MESSAGE

    @allure.title('Проверка невозможности создания пользовател без обязательных полей')
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_impossibility_creating_user_without_required_field(self, missing_field):
        user_data = generate_user_body()
        user_data[missing_field] = None
        response = UserMethods.register(user_data)
        assert response.status_code == 403
        assert response.json() == ErrorMessages.INSUFFICIENT_DATA_CREATE_MESSAGE
