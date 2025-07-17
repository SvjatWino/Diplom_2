import requests
import allure
from data import generate_user
from urls import REGISTER_USER, LOGIN_USER, DELETE_USER

@allure.feature("Логин пользователя")
@allure.story("Тестирование входа с корректными и некорректными данными")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self):
        # Подготовка: регистрация пользователя
        user = generate_user()
        register_response = requests.post(REGISTER_USER, json=user)
        assert register_response.status_code == 200, f"Ошибка при регистрации: {register_response.text}"

        # Вход
        login_response = requests.post(LOGIN_USER, json={
            "email": user["email"],
            "password": user["password"]
        })
        assert login_response.status_code == 200, f"Ошибка при входе: {login_response.text}"
        access_token = login_response.json().get("accessToken")
        assert access_token, "accessToken отсутствует"

        # Очистка: удаление пользователя
        headers = {"Authorization": access_token}
        delete_response = requests.delete(DELETE_USER, headers=headers)
        assert delete_response.status_code == 202, f"Пользователь не удалён: {delete_response.text}"

    @allure.title("Вход с некорректным логином и паролем")
    def test_login_invalid_credentials(self):
        invalid_user = {
            "email": "wrong_email@example.com",
            "password": "wrongpassword"
        }

        response = requests.post(LOGIN_USER, json=invalid_user)

        assert response.status_code == 401, f"Ожидался 401, но получен {response.status_code}"
        assert response.json().get("message") == "email or password are incorrect", \
            f"Неожиданное сообщение об ошибке: {response.text}"
