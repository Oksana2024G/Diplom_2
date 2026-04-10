import allure
import pytest
import requests
from data import ErrorMessages, Ingredients
from methods.order_methods import OrderMethods


@allure.title('Создание заказа с авторизацией и с ингредиентами')
def test_create_order_authorized_with_ingredients(create_user_and_get_token):
    user_data, access_token = create_user_and_get_token
    response = OrderMethods.create_order(Ingredients.correct_list_of_ingredients, access_token)
    assert response.status_code == 200
    assert response.json()["success"] == True

@allure.title("Создание заказа без авторизации с ингредиентами")
def test_create_order_unauthorized_with_ingredients():
    response = OrderMethods.create_order(Ingredients.correct_list_of_ingredients)
    # Здесь реально Баг, проверяла в Postman. ОР: только авторизованные пользователи могут делать заказы, ФР: заказ создается без создания и авторизации пользователя
    assert response.status_code == 401
    assert response.json() == ErrorMessages.NO_AUTHORIZATION_MESSAGE

@allure.title("Создание заказа с авторизацией, но без ингредиентов")
def test_create_order_authorized_without_ingredients(create_user_and_get_token):
    user_data, access_token = create_user_and_get_token
    response = OrderMethods.create_order(Ingredients.empty_list_of_ingredients, access_token)
    assert response.status_code == 400
    assert response.json() == ErrorMessages.NO_INGREDIENT_MESSAGE

@allure.title("Создание заказа с авторизацией и неверными ингредиентами")
def test_create_order_authorized_with_invalid_ingredients(create_user_and_get_token):
    user_data, access_token = create_user_and_get_token
    response = OrderMethods.create_order(Ingredients.list_of_ingredients_incorrect_hash, access_token)
    assert response.status_code == 500
