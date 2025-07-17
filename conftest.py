import pytest
import requests
from data import generate_user
from urls import REGISTER_USER, LOGIN_USER

@pytest.fixture
def new_user():
    user = generate_user()
    response = requests.post(REGISTER_USER, json=user)
    assert response.status_code == 200
    return user

@pytest.fixture
def access_token(new_user):
    response = requests.post(LOGIN_USER, json={
        "email": new_user["email"],
        "password": new_user["password"]
    })
    assert response.status_code == 200
    return response.json()["accessToken"]
