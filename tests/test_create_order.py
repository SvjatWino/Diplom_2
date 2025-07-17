import requests
from urls import CREATE_ORDER
from data import VALID_INGREDIENTS, INVALID_INGREDIENTS
import allure

@allure.feature("Создание заказа")
@allure.story("Тестирование создания заказа с различными условиями")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.post(CREATE_ORDER, json={"ingredients": VALID_INGREDIENTS}, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_unauthorized(self):
        response = requests.post(CREATE_ORDER, json={"ingredients": VALID_INGREDIENTS})
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами без авторизации")
    def test_create_order_with_ingredients_unauthorized(self):
        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
        }

        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_no_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.post(CREATE_ORDER, json={"ingredients": []}, headers=headers)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидными ингредиентами")
    def test_create_order_invalid_ingredients(self, access_token):
        headers = {"Authorization": access_token}
        response = requests.post(CREATE_ORDER, json={"ingredients": INVALID_INGREDIENTS}, headers=headers)
        assert response.status_code in [400, 500]
