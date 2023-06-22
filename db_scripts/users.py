#!/usr/bin/python3
import requests
import json
"""
=================================
Puebla la db con varios usuarios.
=================================

Para usar este script debes cambiar el valor de la
variable @port por el numer0 del puerto donde
tengas levantada la API.
"""


user_list = []
port = 8000

for x in range(25):
    url = f"http://127.0.0.1:{port}/api/signup/"
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
