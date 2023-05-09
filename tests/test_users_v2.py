import pytest
# from pytest_steps import test_steps
from endpoints import users_v2
from assertpy.assertpy import assert_that
from uuid import uuid4
import requests
from cerberus import Validator  # A library used to help schema validations
import json
from schemas import all_schemas, schema_validator




def test_get_all_users():
        response_data = users_v2.get_all_users()
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        response_text = response_data.json()
        assert_that(response_text).extracting("email").is_not_empty()
        # response_text=json.load(response_data)

        # assert that the response body meets the set schema
        valid, errors = schema_validator.schema_data_validator(response_text, all_schemas.users_schema)
        assert_that(valid, description=errors).is_true()


def test_create_new_user():
        email = f"{str(uuid4())}@testacrolinx.com"
        response_data = users_v2.create_new_user(email)
        # users = users_v2.get_all_users()
        # users_v2.search_created_user(users.json(), response_data)
        assert_that(response_data.status_code, description='Person not created').is_equal_to(requests.codes.created)
        assert_that(response_data.json()['email']).contains(email)

        # validate the response body is equivalent to the set schema.
        valid, errors = schema_validator.schema_data_validator(response_data.json(), all_schemas.users_schema)
        assert_that(valid, description=errors).is_true()

        # verify that the same email can not be used more than once
        response_message = users_v2.create_new_user(email)
        assert_that(response_message.json()).extracting("message").contains("has already been taken")

def test_delete_user():
        email = f"{str(uuid4())}@testacrolinx.com"
        response_data = users_v2.create_new_user(email)
        response_text = response_data.json()

        print(response_data.json())
        deleted_user = users_v2.delete_user(response_text['id'])
        assert_that(deleted_user.status_code, description='User not deleted').is_equal_to(requests.codes.no_content)

        # checking if the correct error message is displayed when you try to delete the same user for the second time.
        second_deleted_user = users_v2.delete_user(response_text['id'])
        resp = second_deleted_user.json()
        assert_that(resp["message"]).contains("Resource not found")