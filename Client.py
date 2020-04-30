import requests


def get(function):
    return requests.get('http://127.0.0.1:5000/{}'.format(function)).json()


def post(function, json):
    return requests.post('http://127.0.0.1:5000/{}'.format(function), json=json).json()


print(post('login', {'universe': 'UNI', 'username': 'USER', 'password': 'PASSWORD'}))
print(get('attacked'))
print(post('supply', {'id': 12345}))
print(get('logout'))
