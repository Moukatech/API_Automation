import json
import requests
from config import BASEURL

def get_users_data():
    url = f"{BASEURL}/v1/users"

    session = requests.session()
    response = session.get(url, verify=True)

    return response

#get_users_data()