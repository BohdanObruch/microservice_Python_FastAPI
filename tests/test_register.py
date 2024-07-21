import allure
from api.user_api import UserApi
from data.register_data import UNSUCCESSFUL_REGISTER, SUCCESSFUL_REGISTER
import json


@allure.title("Unsuccessful registration and check response error message")
def test_unsuccessful_register():
    response = UserApi().register(UNSUCCESSFUL_REGISTER.model_dump())
    assert response.status_code == 400
    assert json.loads(response.body)['detail'] == 'Missing email'


@allure.title("Successful registration")
def test_successful_register():
    response = UserApi().register(SUCCESSFUL_REGISTER.model_dump())
    assert response.status_code == 200
    assert json.loads(response.body)['message'] == 'Successfully registered'
