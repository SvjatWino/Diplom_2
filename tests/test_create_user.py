import requests
import allure
from data import generate_user
from urls import REGISTER_USER

@allure.feature("Создание пользователя")
@allure.story("Регистрация с разными условиями")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user = generate_user()
        response = requests.post(REGISTER_USER, json=user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self):
        user = generate_user()

        first_response = requests.post(REGISTER_USER, json=user)
        assert first_response.status_code == 200

        second_response = requests.post(REGISTER_USER, json=user)
        assert second_response.status_code == 403
        assert second_response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя с пустым обязательным полем (пароль)")
    def test_create_user_without_password(self):
        user = generate_user()
        user["password"] = ""

        response = requests.post(REGISTER_USER, json=user)

        assert response.status_code in [400, 403], f"Ожидался 400 или 403, но получен {response.status_code}"
        assert response.json()["message"] == "Email, password and name are required fields", \
            f"Неожиданное сообщение об ошибке: {response.text}"