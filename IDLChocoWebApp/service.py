import re

import requests

IDLAPI = 'https://idlreasoner-choco-api.herokuapp.com/api/'


def generate_request(url, json, params={}):
    url += '?'
    for (key, value) in params.items():
        if key == "request":
            url += value
        else:
            url += key + '=' + str(value) + '&'

    if json is None:
        response = requests.get(url)
    else:
        url = url[:-1]
        response = requests.post(url, data=json)

    return response


def invoke_api(form):
    request = ""
    if form.cleaned_data.get('request') is not None and form.cleaned_data.get('request') != '':
        params = form.cleaned_data.get('request').split('&')
        for param in params:
            param = param.split('=', 1)
            request += "request[" + param[0] + "]=" + param[1] + "&"
        request = request[:-1]
    params = {'operationPath': form.cleaned_data.get('operation_path'),
              'operationType': form.cleaned_data.get('operation_type')}

    if request is not None:
        params['request'] = request
    if form.cleaned_data.get('parameter') is not None and form.cleaned_data.get('parameter') != '':
        params['parameter'] = form.cleaned_data.get('parameter')

    json = None

    if re.match(r"^http(s)?://+", form.cleaned_data.get('api_specification')):
        params['specificationUrl'] = form.cleaned_data.get('api_specification')
    else:
        json = form.cleaned_data.get('api_specification')

    response = generate_request(IDLAPI + form.cleaned_data.get('analysis_operation'), json, params)

    return response
