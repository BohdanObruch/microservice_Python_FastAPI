import allure
from api.user_api import UserApi
import json
from utils.random_data import get_existing_user_id, get_non_existing_user_id


@allure.title("Delete user")
def test_delete_user():
    user_id = get_existing_user_id()
    response = UserApi().delete_user(user_id)

    assert response.status_code == 204
    assert json.loads(response.body)['message'] == 'User deleted'


@allure.title("Delete user that does not exist")
def test_delete_user_not_found():
    user_id = get_non_existing_user_id()
    response = UserApi().delete_user(user_id)
    assert response.status_code == 404
    response_json = json.loads(response.body)
    assert response_json['detail'] == 'User not found'
