import allure
from api.user_api import UserApi
import json
from utils.random_data import get_existing_user_id, get_non_existing_user_id


@allure.title("Get users")
def test_get_users():
    response = UserApi().get_users()
    response_content = json.loads(response.body)
    assert isinstance(response_content, list)
    assert len(response_content) > 0
    assert response.status_code == 200


@allure.title("Get user by ID")
def test_get_user():
    user_id = get_existing_user_id()
    response = UserApi().get_user(user_id)
    response_content = json.loads(response.body)
    assert isinstance(response_content, dict)
    assert response_content['id'] == user_id
    assert response.status_code == 200


@allure.title("Get user by ID that does not exist")
def test_get_user_not_found():
    user_id = get_non_existing_user_id()
    response = UserApi().get_user(user_id)
    assert response.status_code == 404
    response_json = json.loads(response.body)
    assert response_json['detail'] == 'User not found'
