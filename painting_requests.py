import requests

'''
x = requests.get('http://127.0.0.1:5000')

print(x.json())
'''

def get_users_names():
    response = requests.get('http://127.0.0.1:5000') 
    json_response = response.json()

    usuarios = []

    for usuario in json_response:
        usuarios.append((usuario[1], usuario[2])) 
    
    return usuarios