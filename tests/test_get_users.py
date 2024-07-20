import allure
from api.user_api import user_api
from schemas.user_list_schema import user_list_schema
from schemas.single_user_schema import single_user_schema


@allure.title("Getting users list")
def test_get_users_list():
    user_api.get_list_user().status_code_should_be(200).json_schema_should_be_valid(
        user_list_schema).check_len_user_list(6)


@allure.title("Getting single user by id")
def test_get_single_user():
    user_api.get_user_by_id('2').status_code_should_be(200).json_schema_should_be_valid(
        single_user_schema).have_value_in_response_parameter('id', 2)


@allure.title("Getting single user by failed id")
def test_get_single_user_failed():
    user_api.get_user_by_id('100').status_code_should_be(404)
