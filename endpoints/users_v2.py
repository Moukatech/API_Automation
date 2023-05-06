import json
import requests
from uuid import uuid4
from config import BASEURL
from assertpy.assertpy import assert_that


def get_all_users():
    url = f"{BASEURL}/v2/users"

    session = requests.session()
    response = session.get(url, verify=True)

    return response


def create_new_user():
    email = f"{str(uuid4())}@testacrolinx.com"
    url = f"{BASEURL}/v2/users"
    payload = json.dumps({
        "name": "Lamouka",
        "gender": "male",
        "email": email,
        "status": "active"
    })
    headers = {
        'Authorization': 'Bearer 85b48914126e8e5e22425a763b21c19a34da5a9b62edbd7b4ff21addb2a94092',
        'Content-Type': 'application/json'
    }
    session = requests.session()
    response = session.post(url, headers=headers, data=payload, verify=True)
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.created)
    return email, response


def delete_user(user_id):
    url = f"{BASEURL}/v2/users/{user_id}"
    headers = {
        'Authorization': 'Bearer 85b48914126e8e5e22425a763b21c19a34da5a9b62edbd7b4ff21addb2a94092',
        'Content-Type': 'application/json'
    }
    session = requests.session()
    response = session.delete(url, headers=headers, verify=True)
    return response

def search_created_user(users, email):
    for i in users:
        for value in i.values():
            # print every key of each dict
            # if key['email'] == email:
            print(value)
    # return [user for user in users if user['email'] == email]
