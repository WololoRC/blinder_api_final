#!/usr/bin/python3
import requests
import json
"""Create some users for testing and development"""


user_list = []

for x in range(25):
    url = "http://127.0.0.1:8000/api/signup/"
    data = {
        'username': f"user{x}",
        'password': f"pwd{x}",
        'birth_date': "1997-4-2"
    }
    r = requests.post(url, json=data)
    print(r.json())
    user_list.append(r.json())

with open('user_tokens.json', 'w', encoding='utf-8') as a_file:
    json.dump(user_list, a_file)
