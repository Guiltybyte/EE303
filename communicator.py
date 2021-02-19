import requests


def get_random_destination():
    r = requests.get('http://54.78.246.30:8081/api/random-destination/af675841') # noqa
    print("status: ", r.status_code)
    print("random_position", r.text)
