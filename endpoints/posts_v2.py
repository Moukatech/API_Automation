import json
import requests
from uuid import uuid4
from config import BASEURL
from assertpy.assertpy import assert_that

headers = {
        'Authorization': 'Bearer 85b48914126e8e5e22425a763b21c19a34da5a9b62edbd7b4ff21addb2a94092',
        'Content-Type': 'application/json'
    }

def get_all_posts():
    url = f"{BASEURL}/v2/posts"

    session = requests.session()
    response = session.get(url, verify=True)

    return response


def create_new_post(user_id):
    
    url = f"{BASEURL}/v2/posts"
    payload = json.dumps({
        "user_id": user_id,
        "title": "We are here to test",
        "body": "testing for all"
})
    
    session = requests.session()
    response = session.post(url, headers=headers, data=payload, verify=True)
    
    return response


def delete_post(post_id):
    url = f"{BASEURL}/v2/posts/{post_id}"
    session = requests.session()
    response = session.delete(url, headers=headers, verify=True)
    return response

def search_created_post(users, email):
    for i in users:
        for value in i.values():
            # print every key of each dict
            # if key['email'] == email:
            print(value)
    # return [user for user in users if user['email'] == email]
