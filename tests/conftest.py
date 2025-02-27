import pytest
import requests
from generators import generate_user_body
from methods.user_methods import UserMethods


@pytest.fixture(scope="function")
def create_user_and_get_token():
    user_data = generate_user_body()
    register_response = UserMethods.register(user_data)
    access_token = register_response.json().get("accessToken")
    yield user_data, access_token  # возвращаем user_data и accessToken

    # Удаляем пользователя после выполнения теста
@pytest.fixture(scope="function")
def delete_user(create_user_and_get_token):
    user_data, access_token = create_user_and_get_token
    yield
    UserMethods.delete_user(access_token)
