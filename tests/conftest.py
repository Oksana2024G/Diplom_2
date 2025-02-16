import pytest
import requests
from generators import generate_user_body
from methods.auth_methods import AuthMethods
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@pytest.fixture()
def user_methods():
    return UserMethods()

@pytest.fixture()
def auth_methods():
    return AuthMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

@pytest.fixture(scope="function")
def create_user_and_get_token(user_methods):
    user_data = generate_user_body()
    register_response = user_methods.register(user_data)
    if register_response.status_code == 200:
        access_token = register_response.json().get("accessToken")
        yield user_data, access_token  # возвращаем user_data и accessToken
    else:
        raise Exception(f"User creation failed: {register_response.status_code} - {register_response.text}")

    # Удаляем пользователя после выполнения теста
@pytest.fixture(scope="function")
def delete_user(create_user_and_get_token, user_methods):
    user_data, access_token = create_user_and_get_token
    yield
    delete_response = user_methods.delete_user(access_token)
    assert delete_response.status_code == 200
