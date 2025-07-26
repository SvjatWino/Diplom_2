import requests
import allure
import pytest
from data import generate_user, USER_ERROR_MESSAGE_ALREADY_EXISTS, USER_ERROR_MESSAGE_REQUIRED_FIELDS, USER_ERROR_STATUS_CODES
from urls import REGISTER_USER

@allure.feature("Создание пользователя")
@allure.story("Регистрация с разными условиями")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        user = generate_user()
        with allure.step("Отправка запроса на создание уникального пользователя"):
            response = requests.post(REGISTER_USER, json=user)
        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self):
        user = generate_user()

        with allure.step("Регистрация нового пользователя"):
            first_response = requests.post(REGISTER_USER, json=user)
        with allure.step("Проверка успешной регистрации"):
            assert first_response.status_code == 200

        with allure.step("Повторная регистрация того же пользователя"):
            second_response = requests.post(REGISTER_USER, json=user)
        with allure.step("Проверка ошибки 403 и сообщения о существующем пользователе"):
            assert second_response.status_code == 403
            assert second_response.json()["message"] == USER_ERROR_MESSAGE_ALREADY_EXISTS

    @pytest.mark.parametrize("field", ["email", "password", "name"])
    @allure.title("Создание пользователя с отсутствующим обязательным полем")
    def test_create_user_missing_required_field(self, field):
        user = generate_user()
        user[field] = ""

        with allure.step(f"Отправка запроса на создание пользователя без обязательного поля: {field}"):
            response = requests.post(REGISTER_USER, json=user)

        with allure.step("Проверка кода ответа и сообщения об ошибке"):
            assert response.status_code in USER_ERROR_STATUS_CODES, \
                f"Ожидался 400 или 403, но получен {response.status_code}"
            assert response.json()["message"] == USER_ERROR_MESSAGE_REQUIRED_FIELDS, \
                f"Неожиданное сообщение об ошибке: {response.text}"
