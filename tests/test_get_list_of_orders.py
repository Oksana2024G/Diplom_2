import allure
import pytest
from data import ErrorMessages
from methods.order_methods import OrderMethods

@allure.title("Получение заказов: авторизованным пользователем")
def test_get_user_orders_authorized(create_user_and_get_token):
    user_data, access_token = create_user_and_get_token
    get_orders_response = OrderMethods.get_user_orders(access_token)
    assert get_orders_response.status_code == 200
    assert get_orders_response.json()["success"] == True

@allure.title("Получение заказов: неавторизованным пользователем")
def test_get_user_orders_unauthorized():
    get_orders_response = OrderMethods.get_user_orders()
    assert get_orders_response.status_code == 401
    assert get_orders_response.json() == ErrorMessages.NO_AUTHORIZATION_MESSAGE
