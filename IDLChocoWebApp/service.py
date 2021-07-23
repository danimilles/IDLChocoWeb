import re

import requests


IDLAPI = 'https://idlreasoner-choco-api.herokuapp.com/'

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def invoke_api(get, form):
    params = {}
    params['operationPath']
    params['operationType']
    params['request']
    params['parameter']
    if re.match(r"^http(s)?://+", form['api_specification']):
        params['specificationUrl'] = form['api_specification']
    else:
        json = form['api_specification']
    response = generate_request(IDLAPI + form['analysis_operation'], None)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return ''