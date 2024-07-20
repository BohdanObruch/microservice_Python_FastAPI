import allure
import requests
from jsonschema import validate


class Api:
    # Base class for API

    _URL = 'https://reqres.in'

    def __init__(self):
        self.response = None

    # METHODS API

    @allure.step("Send POST request")
    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None, headers: dict = None):
        with allure.step(f"POST-request for url: {url}{endpoint}"
                         f"\n request body: \n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=headers,
                                          params=params,
                                          json=json_body)

        return self

    @allure.step("Send GET request")
    def get(self, url: str, endpoint: str, params: dict = None, headers: dict = None):
        with allure.step(f"GET-request for url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params)

        return self

    @allure.step("Send PUT request")
    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None, headers: dict = None):
        with allure.step(f"PUT-request for url: {url}{endpoint}"
                         f"\n request body: \n {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         headers=headers,
                                         params=params,
                                         json=json_body)

        return self

    @allure.step("Send DELETE request")
    def delete(self, url: str, endpoint: str, headers: dict = None):
        with allure.step(f"DELETE-request for url: {url}{endpoint}"):
            self.response = requests.delete(url=f"{url}{endpoint}",
                                            headers=headers)
        return self

        # ASSERTIONS:

    @allure.step("Status code should be {expected_code}")
    def status_code_should_be(self, expected_code: int):
        # Check the status of the response code is equal to the expected code
        actual_code = self.response.status_code
        assert expected_code == actual_code, f"\nExpected status code: {expected_code}" \
                                             f"\nActual status code: {actual_code}"
        return self

    @allure.step("JSON schema should be valid")
    def json_schema_should_be_valid(self, json_schema):
        # Validate the response JSON against the provided JSON schema
        validate(self.response.json(), json_schema)
        return self

    @allure.step("Response parameter {parameter_name} should have value {expected_value}")
    def have_value_in_response_parameter(self, parameter_name: str, expected_value: str):

        api_data = self.response.json()
        actual_value = self.find_value_from_nested_dict(api_data, parameter_name)

        assert actual_value == expected_value, f"\nExpected result: {expected_value}" \
                                               f"\nActual result: {actual_value}"

    def find_value_from_nested_dict(self, dictionary, parameter_name):
        if parameter_name in dictionary:
            return dictionary[parameter_name]

        for value in dictionary.values():
            if isinstance(value, dict):
                nested_value = self.find_value_from_nested_dict(value, parameter_name)

                if nested_value is not None:
                    return nested_value

        return f'Parameter {parameter_name} not found in response'
