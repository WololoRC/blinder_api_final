#!/usr/bin/python3
"""
==================================
Script para poblar db con matches.
==================================

Antes de leer esta documentacion lee la del
script 'users.py'

Para usar este script debes primero tener la api levantada
y ejecutar en el directorio 'db_scripts' el script 'users.py'.

Luego dentro de este mismo archivo cambia el valor de la
variable @port por el numero del puerto donde tengas levantada
la API y ejecuta el script.

con la ruta 'api/chat/inbox/<uuid:profile_id>/' puedes conseguir
todas las instancias de chat relacionadas a un usuario.
"""
import requests
import json

def match_making(id_list):
    i = 0
    port = 8000
    while (i < len(id_list)):
        for cnt, item in enumerate(id_list):
            if id_list[cnt] == id_list[i]:
                pass
            else:
                r = requests.put(
                    f"http://127.0.0.1:{port}/api/profile/like_list/update/{id_list[i]}/",
                    data={'like_id': f"{item}"}
                )
                print(r.json())
        i += 1


id_list = []
cnt = 0

with open('user_tokens.json', 'r', encoding='utf-8') as a_file:
    user_list = json.load(a_file)

for item in user_list:
    id_list.append(item.get('id'))
    cnt += 1
    if cnt == 5:
        break

match_making(id_list)
