import pytest
import requests
import allure
import logging
from data import generate_user
from urls import REGISTER_USER, LOGIN_USER, DELETE_USER

logger = logging.getLogger(__name__)

@pytest.fixture
def new_user():
    with allure.step("Генерация и регистрация нового пользователя"):
        user = generate_user()
        response = requests.post(REGISTER_USER, json=user)
        if response.status_code != 200:
            pytest.fail(f"Не удалось зарегистрировать пользователя: {response.text}")
        return user

@pytest.fixture
def access_token(new_user):
    with allure.step("Получение accessToken для зарегистрированного пользователя"):
        response = requests.post(LOGIN_USER, json={
            "email": new_user["email"],
            "password": new_user["password"]
        })
        if response.status_code != 200:
            pytest.fail(f"Не удалось войти в систему: {response.text}")
        return response.json()["accessToken"]

@pytest.fixture
def registered_user_with_token():
    user = generate_user()

    with allure.step("Регистрация пользователя"):
        register_response = requests.post(REGISTER_USER, json=user)
        if register_response.status_code != 200:
            pytest.fail(f"Ошибка при регистрации: {register_response.text}")

    with allure.step("Логин пользователя"):
        login_response = requests.post(LOGIN_USER, json={
            "email": user["email"],
            "password": user["password"]
        })
        if login_response.status_code != 200:
            pytest.fail(f"Ошибка при входе: {login_response.text}")

        access_token = login_response.json().get("accessToken")
        if not access_token:
            pytest.fail("accessToken отсутствует")

    yield access_token

    with allure.step("Удаление пользователя после теста"):
        headers = {"Authorization": access_token}
        delete_response = requests.delete(DELETE_USER, headers=headers)
        if delete_response.status_code != 202:
            logger.warning(f"Не удалось удалить пользователя: {delete_response.text}")
