import requests
from urls import CREATE_ORDER
from data import (
    INVALID_INGREDIENTS,
    ORDER_PAYLOAD_WITH_INGREDIENTS,
    ORDER_PAYLOAD_WITH_SOME_INGREDIENTS,
    ORDER_PAYLOAD_NO_INGREDIENTS,
    ORDER_ERROR_MESSAGE_NO_INGREDIENTS,
    ORDER_ERROR_STATUS_CODES
)
import allure

@allure.feature("Создание заказа")
@allure.story("Тестирование создания заказа с различными условиями")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, access_token):
        headers = {"Authorization": access_token}
        with allure.step("Отправка POST-запроса на создание заказа с авторизацией"):
            response = requests.post(CREATE_ORDER, json=ORDER_PAYLOAD_WITH_INGREDIENTS, headers=headers)
        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        with allure.step("Отправка POST-запроса на создание заказа без авторизации"):
            response = requests.post(CREATE_ORDER, json=ORDER_PAYLOAD_WITH_INGREDIENTS)
        with allure.step("Проверка успешного ответа"):
            assert response.status_code == 200
            assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами без авторизации")
    def test_create_order_with_ingredients_unauthorized(self):
        with allure.step("Отправка POST-запроса на создание заказа с ингредиентами без авторизации"):
            response = requests.post(CREATE_ORDER, json=ORDER_PAYLOAD_WITH_SOME_INGREDIENTS)
        with allure.step("Проверка успешного ответа и наличия заказа в ответе"):
            assert response.status_code == 200
            assert response.json()["success"] is True
            assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        with allure.step("Отправка POST-запроса на создание заказа без ингредиентов"):
            response = requests.post(CREATE_ORDER, json=ORDER_PAYLOAD_NO_INGREDIENTS, headers=headers)
        with allure.step("Проверка ошибки 400 и сообщения об отсутствии ингредиентов"):
            assert response.status_code == 400
            assert response.json()["message"] == ORDER_ERROR_MESSAGE_NO_INGREDIENTS

    @allure.title("Создание заказа с невалидными ингредиентами")
    def test_create_order_invalid_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        with allure.step("Отправка POST-запроса на создание заказа с невалидными ингредиентами"):
            response = requests.post(CREATE_ORDER, json={"ingredients": INVALID_INGREDIENTS}, headers=headers)
        with allure.step("Проверка ошибки 400 или 500"):
            assert response.status_code in ORDER_ERROR_STATUS_CODES
