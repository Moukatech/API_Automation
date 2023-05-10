import json
import requests
from config import BASEURL


def get_users_data():
    url = f"{BASEURL}/v1/users"

    session = requests.session()
    response = session.get(url, verify=True)

    return response


def get_single_user(user_id):
    url = f"{BASEURL}/v1/users/{user_id}"

    session = requests.session()
    response = session.get(url, verify=True)

    return response

def pagination(page_no):
    url = f"{BASEURL}/v1/users?page={page_no}"

    session = requests.session()
    response = session.get(url, verify=True)

    return response