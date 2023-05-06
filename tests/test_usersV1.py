import pytest
# from pytest_steps import test_steps
from endpoints import users_V1
from assertpy.assertpy import assert_that

# from jsonschema import validate


def test_get_weathermap_city():
        response_data =users_V1.get_users_data()
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        response_text = response_data.json
        assert_that(response_text).extracting("email").contains('balagovind_guha@barton-stiedemann.test')

        # assert validate(res_weather_data.json(), get_weather_data_schema), \
        #     f"Schema Validation failed for {res_weather_data.request.url}"
        # assert (res_weather_data.json()['name'] == 'Pune')