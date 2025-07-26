import requests
import allure
from urls import LOGIN_USER
from data import INVALID_LOGIN_USER, LOGIN_ERROR_MESSAGE_INVALID_CREDENTIALS, LOGIN_ERROR_STATUS_CODE

@allure.feature("Логин пользователя")
@allure.story("Тестирование входа с корректными и некорректными данными")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, registered_user_with_token):
        with allure.step("Проверка, что токен получен"):
            assert registered_user_with_token, "Токен не получен"

    @allure.title("Вход с некорректным логином и паролем")
    def test_login_invalid_credentials(self):
        with allure.step("Попытка входа с некорректными данными"):
            response = requests.post(LOGIN_USER, json=INVALID_LOGIN_USER)

        with allure.step("Проверка ошибки авторизации"):
            assert response.status_code == LOGIN_ERROR_STATUS_CODE, f"Ожидался {LOGIN_ERROR_STATUS_CODE}, но получен {response.status_code}"
            assert response.json().get("message") == LOGIN_ERROR_MESSAGE_INVALID_CREDENTIALS, \
                f"Неожиданное сообщение об ошибке: {response.text}"
