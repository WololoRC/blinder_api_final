#!/usr/bin/python3
import json
import requests
import random

with open('tag_list.json', 'r', encoding='utf-8') as a_file:
    tag_list = json.load(a_file)

with open('user_tokens.json', 'r', encoding='utf-8') as a_file:
    user_list = json.load(a_file)

tag_list = [item.get('id') for item in tag_list]
user_list = [item.get('id') for item in user_list]

for item in user_list:
    tags = random.sample(tag_list, 5)
    data = {
        "add_tags": [
            f"{tags[0]}",
            f"{tags[1]}",
            f"{tags[2]}",
            f"{tags[3]}",
            f"{tags[4]}",
        ],
        'description': 'wololo'
    }
    url = f"http://127.0.0.1:8000/api/profile/{item}/"
    requests.put(url, json=data)

