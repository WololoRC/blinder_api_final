#!/usr/bin/python3
from datetime import date
import requests
import json

data = {
    'birth_age': json.dumps(date(1990,4,10)),
    'description':'Wololo',
    'user_id': 2
}

headers = {
    "Authorization": "Token 1e97344f3453ccac9d6853a0da75931eb9f25e32"
}

url = "http://127.0.0.1:8000/api/profile/"

r = requests.post(url,json=data, headers=headers)
