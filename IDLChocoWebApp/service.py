import requests


IDLAPI = 'https://idlreasoner-choco-api.herokuapp.com/'

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(analysis_operation, params={}):
    response = generate_request(IDLAPI + analysis_operation, params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''