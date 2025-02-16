from faker import Faker
import random


faker = Faker()
def generate_user_body():
    name = faker.first_name()
    email = f"{name}{faker.last_name().lower()}{random.randint(1, 999)}@yandex.ru"
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return {"email": email,
            "password": password,
            "name": name
            }
