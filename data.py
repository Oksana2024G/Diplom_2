class DataForUser:
    CREATE_USER = {
        "email": "test-data@yandex.ru",
        "password": "password",
        "name": "Username"
}

class DataForAuth:
    LOGIN_BODY = {
        "email": "test-data@yandex.ru",
        "password": "password"
}

class DataForOrder:
    CREATE_ORDER_BODY = {
        "ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]
    }

class ErrorMessages:
    INSUFFICIENT_DATA_CREATE_MESSAGE = {"success": False, "message": "Email, password and name are required fields"}
    LOGIN_ALREADY_USED_MESSAGE = {"success": False, "message": "User already exists"}
    INCORRECT_LOGIN_MESSAGE = {"success": False, "message": "email or password are incorrect"}
    NO_AUTHORIZATION_MESSAGE = {"success": False, "message": "You should be authorised"}
    NO_INGREDIENT_MESSAGE = {"success": False, "message": "Ingredient ids must be provided"}

class Ingredients:
    correct_list_of_ingredients = {
        "ingredients": ["61c0c5a71d1f82001bdaaa74", "61c0c5a71d1f82001bdaaa6e", "61c0c5a71d1f82001bdaaa6d"]
        }

    empty_list_of_ingredients = {
        "ingredients": []
        }

    list_of_ingredients_incorrect_hash = {
        "ingredients": ["61c0c5a71d11f82001bdaaa6d"]
        }
