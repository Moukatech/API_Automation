import pytest
# from pytest_steps import test_steps
from endpoints import users_v2
from assertpy.assertpy import assert_that
import requests

# from jsonschema import validate


def test_get_all_users():
        response_data =users_v2.get_all_users()
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        response_text = response_data.json()
        assert_that(response_text).extracting("email").contains('balagovind_guha@barton-stiedemann.test')

        # assert validate(res_weather_data.json(), get_weather_data_schema), \
        #     f"Schema Validation failed for {res_weather_data.request.url}"

def test_create_new_user():
        email, response_data = users_v2.create_new_user()
        print(response_data)
        # users = users_v2.get_all_users()
        # users_v2.search_created_user(users.json(), response_data)
        assert_that(response_data.json()['email']).contains(email)

def test_delete_user():
        email, response_data = users_v2.create_new_user()
        response_text = response_data.json()
        # print(response_text['id'])
        deleted_user = users_v2.delete_user(response_text['id'])
        assert_that(deleted_user.status_code, description='User not deleted').is_equal_to(requests.codes.no_content)

        ## checking if the correct error message is displayed when you try to delete the same user the second time.
        second_deleted_user = users_v2.delete_user(response_text['id'])
        resp =second_deleted_user.json()
        assert_that(resp["message"]).contains("Resource not found")