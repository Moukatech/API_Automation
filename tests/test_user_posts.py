import random

import pytest
# from pytest_steps import test_steps
from endpoints import user_posts_v2, users_v2
from assertpy.assertpy import assert_that
from uuid import uuid4
import requests
from schemas import schema_validator, all_schemas
from cerberus import Validator  # A library used to help schema validations

email = f"{str(uuid4())}@testacrolinx.com"  # generate a random email to be used when creating a new user


@pytest.mark.test_get_all_users_posts
def test_get_all_user_posts():
    
    response = ""
    users_data =users_v2.get_all_users()
    response_text = users_data.json()
    user_id = [user['id'] for user in response_text]
    selected_id = random.choice(user_id) # select random a user id to be used in getting the posts
    
    response_data = user_posts_v2.get_all_user_posts(selected_id)
    response = response_data.json()
    assert (response_data.status_code == 200), f"Status Code validation failed , Rather found : {response_data.status_code}"
    
    if not response:
        # creates a new post for a user without a post
        resp = user_posts_v2.create_new_post(selected_id)
        assert_that(resp.json()['user_id']).is_equal_to(selected_id)
        assert_that(resp.json()).is_not_empty()
        response = resp.json()

    # validate the response body is equivalent to the set schema.
    valid, errors = schema_validator.schema_data_validator(response, all_schemas.posts_schema)
    assert_that(valid, description=errors).is_true()


@pytest.mark.test_create_new_post
def test_create_new_post_for_user():
        
    user_data = users_v2.create_new_user(email)  # create a new user to used to create a new post
    user_id = user_data.json()["id"]

    # create a new post with the user created before.
    response_data = user_posts_v2.create_new_post(user_id)
    assert_that(response_data.status_code, description='post was not created').is_equal_to(requests.codes.created)
    assert_that(response_data.json()['user_id']).is_equal_to(user_id)

    # validate the response body is equivalent with the set schema.
    valid, errors = schema_validator.schema_data_validator(response_data.json(), all_schemas.posts_schema)
    assert_that(valid, description=errors).is_true()
    