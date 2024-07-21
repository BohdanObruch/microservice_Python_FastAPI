from datetime import datetime

import allure
from api.user_api import user_api
from utils.random_data import get_existing_user_id, get_non_existing_user_id
from data.update_data import unsuccessful_update, successful_update
import json
import pytest

existing_id = get_existing_user_id()
non_existing_id = get_non_existing_user_id()


@allure.title("Unsuccessful update user and check response error message")
@pytest.mark.parametrize("update_method", ["update_put_user", "update_patch_user"])
def test_unsuccessful_update_user(update_method):
    update_data = unsuccessful_update()
    response = getattr(user_api, update_method)(non_existing_id, update_data.model_dump())
    assert response.status_code == 404
    assert json.loads(response.body)['detail'] == 'User not found'


def generate_update_combinations():
    update = successful_update()
    return [
        pytest.param({"email": update.email}, id="update_email"),
        pytest.param({"first_name": update.first_name}, id="update_first_name"),
        pytest.param({"last_name": update.last_name}, id="update_last_name"),
        pytest.param({"avatar": update.avatar}, id="update_avatar"),
        pytest.param({"email": update.email, "first_name": update.first_name},
                     id="update_email_first_name"),
        pytest.param({"email": update.email, "last_name": update.last_name},
                     id="update_email_last_name"),
        pytest.param({"email": update.email, "avatar": update.avatar},
                     id="update_email_avatar"),
        pytest.param({"first_name": update.first_name, "last_name": update.last_name},
                     id="update_first_name_last_name"),
        pytest.param({"first_name": update.first_name, "avatar": update.avatar},
                     id="update_first_name_avatar"),
        pytest.param({"last_name": update.last_name, "avatar": update.avatar},
                     id="update_last_name_avatar"),
        pytest.param({"email": update.email, "first_name": update.first_name,
                      "last_name": update.last_name},
                     id="update_email_first_name_last_name"),
        pytest.param({"email": update.email, "first_name": update.first_name,
                      "avatar": update.avatar},
                     id="update_email_first_name_avatar"),
        pytest.param({"email": update.email, "last_name": update.last_name,
                      "avatar": update.avatar},
                     id="update_email_last_name_avatar"),
        pytest.param(
            {"first_name": update.first_name, "last_name": update.last_name,
             "avatar": update.avatar},
            id="update_first_name_last_name_avatar"),
        pytest.param({"email": update.email, "first_name": update.first_name,
                      "last_name": update.last_name,
                      "avatar": update.avatar}, id="update_all_fields")
    ]


@pytest.mark.parametrize("update_method", ["update_put_user", "update_patch_user"])
@pytest.mark.parametrize("update_data", generate_update_combinations())
def test_successful_update_user(update_method, update_data):
    existing_id = get_existing_user_id()

    response = getattr(user_api, update_method)(existing_id, update_data)
    assert response.status_code == 200
    response_json = json.loads(response.body)

    updated_at = response_json['updatedAt']
    expected_updated_at = datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%dT%H:%M:%S')
    assert updated_at.startswith(expected_updated_at)
