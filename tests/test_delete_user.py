import allure
from api.user_api import user_api


@allure.title("Delete user")
def test_delete_user():
    user_api.delete_user('2').status_code_should_be(204)
