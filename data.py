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
