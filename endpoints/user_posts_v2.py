import json
import requests
from uuid import uuid4
from config import BASEURL
from assertpy.assertpy import assert_that


def get_all_user_posts(user_id):
    url = f"{BASEURL}/v2/users/{user_id}/posts"
    session = requests.session()
    response = session.get(url, verify=True)

    return response


def create_new_post(user_id):
    
    url = f"{BASEURL}/v2/users/{user_id}/posts"
    payload = json.dumps({
        "title": "We are here to test",
        "body": "testing for all"
})
    headers = {
        'Authorization': 'Bearer 85b48914126e8e5e22425a763b21c19a34da5a9b62edbd7b4ff21addb2a94092',
        'Content-Type': 'application/json'
    }
    session = requests.session()
    response = session.post(url, headers=headers, data=payload, verify=True)
    
    return response
