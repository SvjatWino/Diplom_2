import random
import string

def generate_user():
    email = f"user_{random.randint(1000, 9999)}@test.ru"
    password = "123456"
    name = ''.join(random.choices(string.ascii_letters, k=6))
    return {
        "email": email,
        "password": password,
        "name": name
    }

INVALID_USER = {
    "email": "wrong@test.ru",
    "password": "wrongpass"
}

USER_WITHOUT_EMAIL = {
    "password": "123456",
    "name": "NoEmail"
}

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",  # Булка
    "61c0c5a71d1f82001bdaaa6f"   # Соус
]

INVALID_INGREDIENTS = [
    "invalid_id_1",
    "invalid_id_2"
]

# Вынес payload и ожидаемые сообщения из тестов создания заказа
ORDER_PAYLOAD_WITH_INGREDIENTS = {
    "ingredients": VALID_INGREDIENTS
}

ORDER_PAYLOAD_WITH_SOME_INGREDIENTS = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}

ORDER_PAYLOAD_NO_INGREDIENTS = {
    "ingredients": []
}

ORDER_ERROR_MESSAGE_NO_INGREDIENTS = "Ingredient ids must be provided"
ORDER_ERROR_STATUS_CODES = [400, 500]
USER_ERROR_MESSAGE_ALREADY_EXISTS = "User already exists"
USER_ERROR_MESSAGE_REQUIRED_FIELDS = "Email, password and name are required fields"
USER_ERROR_STATUS_CODES = [400, 403]
INVALID_LOGIN_USER = {
    "email": "wrong_email@example.com",
    "password": "wrongpassword"
}

LOGIN_ERROR_MESSAGE_INVALID_CREDENTIALS = "email or password are incorrect"
LOGIN_ERROR_STATUS_CODE = 401
