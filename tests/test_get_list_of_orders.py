import allure
import pytest
import helper
from data import ErrorMessages

@allure.title("Получение заказов: авторизованным пользователем")
def test_get_user_orders_authorized(create_user_and_get_token, order_methods):
    user_data, access_token = create_user_and_get_token
    get_orders_response = order_methods.get_user_orders(access_token)
    assert get_orders_response.status_code == 200
    assert get_orders_response.json()["success"] == True

@allure.title("Получение заказов: неавторизованным пользователем")
def test_get_user_orders_unauthorized(order_methods):
    get_orders_response = order_methods.get_user_orders()
    assert get_orders_response.status_code == 401
    assert get_orders_response.json()["message"] == ErrorMessages.NO_AUTHORIZATION_MESSAGE # Баг:  структура ответа не соответствует API документации
