import allure
from api.user_api import user_api
from data.register_data import UNSUCCESSFUL_REGISTER
from schemas.register_schema import unsuccessful_register_schema


@allure.title("Unsuccessful registration and check response error message")
def test_unsuccessful_register():
    (user_api.unsuccessful_register(UNSUCCESSFUL_REGISTER.model_dump())
     .status_code_should_be(400)
     .json_schema_should_be_valid(unsuccessful_register_schema)
     .have_value_in_response_parameter('error', 'Missing password'))
