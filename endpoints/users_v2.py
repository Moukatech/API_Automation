import json
import requests
import random
from uuid import uuid4
from config import BASEURL
from assertpy.assertpy import assert_that

headers = {
        'Authorization': 'Bearer 85b48914126e8e5e22425a763b21c19a34da5a9b62edbd7b4ff21addb2a94092',
        'Content-Type': 'application/json'
    }

def get_all_users():
    url = f"{BASEURL}/v2/users"

    response = requests.get(url, verify=True)

    return response

def get_single_user(user_id):
    url = f"{BASEURL}/v2/users/{user_id}"

    response = requests.get(url, verify=True)

    return response

def create_new_user(email):
    gender = ["Male", "Female"]
    random_gender = random.choice(gender)
    random_no = random.randint(0, 1000) 
    

    url = f"{BASEURL}/v2/users"
    payload = json.dumps({
        "name": f"Lamouka{random_no}",
        "gender": random_gender,
        "email": email,
        "status": "active"
    })

    response = requests.post(url, headers=headers, data=payload, verify=True)
    
    return response


def delete_user(user_id):
    url = f"{BASEURL}/v2/users/{user_id}"

    response = requests.delete(url, headers=headers, verify=True)
    return response

def search_created_user(users, email):
    for i in users:
        for value in i.values():
            # print every key of each dict
            # if key['email'] == email:
            print(value)
    # return [user for user in users if user['email'] == email]
