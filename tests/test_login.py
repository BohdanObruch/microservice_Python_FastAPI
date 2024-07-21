import allure
from api.user_api import UserApi
from data.login_data import UNSUCCESSFUL_LOGIN, SUCCESSFUL_LOGIN
import json


@allure.title("Unsuccessful login and check response error message")
def test_unsuccessful_login():
    response = UserApi().login(UNSUCCESSFUL_LOGIN.model_dump())
    assert response.status_code == 400
    assert json.loads(response.body)['detail'] == 'Missing email'


@allure.title("Successful login")
def test_successful_login():
    response = UserApi().login(SUCCESSFUL_LOGIN.model_dump())
    assert response.status_code == 200
    assert json.loads(response.body)['message'] == 'Successfully logged in'
    assert 'token' in json.loads(response.body)
    assert 'user' in json.loads(response.body)
