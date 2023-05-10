import pytest
# from pytest_steps import test_steps
import json
from endpoints import users_v1
from assertpy.assertpy import assert_that
import random

# from jsonschema import validate


def test_get_all_users():
        response_data = users_v1.get_users_data()
        assert (response_data.status_code == 200), f"Status Code validation failed , Rather found : {response_data.status_code}"

        # loads the json response to a python dict
        response_text = json.loads(response_data.text)
        assert_that(response_text["data"]).extracting("email").is_not_empty() ## asserts that the data is not empty


def test_single_user():
        user_ids =[1537133, 1537130, 859684, 1301273, 2841, 1090]
        selected_id = random.choice(user_ids)
        response_data = users_v1.get_single_user(selected_id)

        response_text = json.loads(response_data.text)
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        assert_that(response_text["data"]["id"]).is_equal_to(selected_id)

def test_pagination():
        page_numbers = [20, 200, 150, 200, 250, 300]
        selected_id = random.choice(page_numbers)
        response_data = users_v1.pagination(selected_id)

        response_text = json.loads(response_data.text)
        assert (response_data.status_code == 200), f"Status Code validation failed for {response_data.request.url}"
        assert_that(response_text["meta"]["pagination"]["links"]["current"]).is_equal_to(response_data.request.url)