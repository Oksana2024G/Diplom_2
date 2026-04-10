import allure
import pytest
import random
from data import ErrorMessages
from generators import generate_user_body
from methods.user_methods import UserMethods

@allure.title('Проверка успешного изменения данных пользователя с авторизацией')
@pytest.mark.parametrize("field_to_change, new_value", [
    ("email", f"new{random.randint(1, 999)}email{random.randint(1, 999)}@yandex.ru"),
    ("password", "dragon25"),
    ("name", "Dayneris")
])

def test_change_user_data_authorized(create_user_and_get_token, field_to_change, new_value):
    user_data, access_token = create_user_and_get_token
    update_data = {field_to_change: new_value}  # Подготавливаем данные для замены
    change_response = UserMethods.change_user_data(access_token, update_data)
    assert change_response.status_code == 200
    assert change_response.json()["success"] == True

@allure.title('Проверка невозможности изменения данных пользователя без авторизации')
def test_change_user_data_unauthorized():
    user_data = generate_user_body()
    response = UserMethods.change_user_data_unauthorized(user_data)
    assert response.status_code == 401
    assert response.json() == ErrorMessages.NO_AUTHORIZATION_MESSAGE
