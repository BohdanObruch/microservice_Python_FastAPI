import allure
from api.user_api import user_api
from data.user_data import USER_DATA, create_user_data
import json
import pytest


optional_combinations = [
    pytest.param({"last_name": "", "avatar": ""}, id="no_last_name_no_avatar"),
    pytest.param({"last_name": create_user_data().last_name, "avatar": ""}, id="last_name_no_avatar"),
    pytest.param({"last_name": "", "avatar": create_user_data().avatar}, id="no_last_name_avatar"),
    pytest.param({"last_name": create_user_data().last_name, "avatar": create_user_data().avatar},
                 id="last_name_avatar")
]


@pytest.mark.parametrize("optional_fields", optional_combinations)
@allure.title('Create user with optional fields')
def test_create_user(optional_fields):
    user_data = create_user_data().model_dump()
    user_data.update(optional_fields)
    response = user_api.create_user(user_data)
    assert response.status_code == 201
    response_json = json.loads(response.body)
    assert response_json['first_name'] == user_data['first_name']
    assert response_json['email'] == user_data['email']
    assert response_json['avatar'] == user_data['avatar']


@pytest.mark.parametrize("missing_field", ["first_name", "email"])
@allure.title('Create user with missing {missing_field}')
def test_create_user_missing_field(missing_field):
    user_data = USER_DATA.model_dump()
    user_data.pop(missing_field)
    response = user_api.create_user(user_data)
    assert response.status_code == 400
    response_json = json.loads(response.body)
    assert response_json['detail'] == f'Missing {missing_field}'
