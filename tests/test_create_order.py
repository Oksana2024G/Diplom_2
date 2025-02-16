import allure
import pytest
import helper
import requests
from data import ErrorMessages, Ingredients

@allure.title('Создание заказа с авторизацией и с ингредиентами')
def test_create_order_authorized_with_ingredients(create_user_and_get_token, order_methods):
    user_data, access_token = create_user_and_get_token
    response = order_methods.create_order(Ingredients.correct_list_of_ingredients, access_token)
    assert response.status_code == 200
    assert response.json()["success"] == True

@allure.title("Создание заказа без авторизации с ингредиентами")
def test_create_order_unauthorized_with_ingredients(order_methods):
    response = order_methods.create_order(Ingredients.correct_list_of_ingredients)
    assert response.status_code == 401                                              # Баг: только авторизованные пользователи могут делать заказы.
    assert response.json().get("message") == ErrorMessages.NO_AUTHORIZATION_MESSAGE

@allure.title("Создание заказа с авторизацией, но без ингредиентов")
def test_create_order_authorized_without_ingredients(create_user_and_get_token, order_methods):
    user_data, access_token = create_user_and_get_token
    response = order_methods.create_order(Ingredients.empty_list_of_ingredients, access_token)
    assert response.status_code == 400
    assert response.json().get("message") == ErrorMessages.NO_INGREDIENT_MESSAGE # Баг:  структура ответа не соответствует API документации

@allure.title("Создание заказа с авторизацией и неверными ингредиентами")
def test_create_order_authorized_with_invalid_ingredients(create_user_and_get_token, order_methods):
    user_data, access_token = create_user_and_get_token
    response = order_methods.create_order(Ingredients.list_of_ingredients_incorrect_hash, access_token)
    assert response.status_code == 500
