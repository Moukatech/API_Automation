import pytest
# from pytest_steps import test_steps
import json
from endpoints import users_v1
from assertpy.assertpy import assert_that

# from jsonschema import validate


def test_get_all_users():
        response_data = users_v1.get_users_data()
        assert (response_data.status_code == 200), f"Status Code validation failed , Rather found : {response_data.status_code}"

        # loads the json response to a python dict
        response_text = json.loads(response_data.text)
        assert_that(response_text["data"]).extracting("email").is_not_empty() ## asserts that the data is not empty

