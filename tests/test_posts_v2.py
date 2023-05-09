import pytest
# from pytest_steps import test_steps
from endpoints import posts_v2, users_v2
from assertpy.assertpy import assert_that
from uuid import uuid4
import requests
from schemas import all_schemas,schema_validator
from cerberus import Validator




def test_get_all_posts():
        response_data =posts_v2.get_all_posts()
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        response_text = response_data.json()
        assert_that(response_text).extracting("title").is_not_empty()
        # response_text=json.load(response_data)

        # validate the response body is equivalent to the set schema.
        valid, errors = schema_validator.schema_data_validator(response_text, all_schemas.posts_schema)
        assert_that(valid, description=errors).is_true()


def test_create_new_post():
        email = f"{str(uuid4())}@testacrolinx.com"
        # create a new user to be used to create a new post
        user_data = users_v2.create_new_user(email)
        user_id = user_data.json()["id"]

        # create a new post for the new user created.
        response_data = posts_v2.create_new_post(user_id)
        assert_that(response_data.status_code, description='post was not created').is_equal_to(requests.codes.created)
        assert_that(response_data.json()['user_id']).is_equal_to(user_id)

        # validate the response body is equivalent to the set schema.
        valid, errors = schema_validator.schema_data_validator(response_data.json(), all_schemas.posts_schema)
        assert_that(valid, description=errors).is_true()


def test_delete_post():
        email = f"{str(uuid4())}@testacrolinx.com"
        # create a new user to be used.
        user_data = users_v2.create_new_user(email)
        user_id = user_data.json()["id"]

        # create a new post
        response_data = posts_v2.create_new_post(user_id)
        response_text = response_data.json()

        # delete the created post.
        deleted_post = posts_v2.delete_post(response_text['id'])
        assert_that(deleted_post.status_code, description='post not deleted').is_equal_to(requests.codes.no_content)

        # checking if the correct error message is displayed when you try to delete the same post the second time.
        second_deleted_user = posts_v2.delete_post(response_text['id'])
        resp = second_deleted_user.json()
        assert_that(resp["message"]).contains("Resource not found")