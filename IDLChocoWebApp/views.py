import re

from django.shortcuts import render, redirect

# Create your views here.
from IDLChocoWebApp.forms import IDLForm
from IDLChocoWebApp.service import invoke_api


def index(request):
    form = IDLForm()
    if request.method == 'POST':
        form = IDLForm(data=request.POST)

        if form.is_valid():
            if (form.cleaned_data.get('analysis_operation') == 'isFalseOptional' or form.cleaned_data.get(
                    'analysis_operation') == 'isDeadParameter') \
                    and (form.cleaned_data.get('parameter') is None or form.cleaned_data.get('parameter') == ''):
                form.add_error('parameter', 'For this operation field Parameter is required')
            elif (form.cleaned_data.get('analysis_operation') == 'isValidRequest' or form.cleaned_data.get(
                    'analysis_operation') == 'isValidPartialRequest') \
                    and (form.cleaned_data.get('request') is None or form.cleaned_data.get('request') == ''):
                form.add_error('request', 'For this operation field Request is required')
            else:
                response = invoke_api(form)
                form.clean()
                return render(request, 'index.html',
                          {'form': form, 'response': parse_response(response, form.cleaned_data.get('operation_path'),
                                                                    form.cleaned_data.get('analysis_operation'))})
    return render(request, 'index.html', {'form': form})


def parse_response(response, operation_path, analysis_operation):
    if response is None:
        res = {'msg': "Can't establish the connection with the API", 'err': True}
        return res

    if response.status_code != 200:
        if response.content is not None and str(response.content) != 'b\'\'':
            res = {'msg': "There was an error analyzing the specification: " +
                          (response.json()['message'] if 'message' in response.json() else response.json()['error']),
                   'err': True}
        res = {'msg': "There was an error analyzing the specification", 'err': True}
        return res
    else:
        res = {}
        if analysis_operation == 'isValidSpecification':
            valid = response.json()['valid']
            res['msg'] = "The specification is "
            res['msg'] += "valid!" if valid else "not valid!"
        elif analysis_operation == 'isValidPartialRequest' or analysis_operation == 'isValidRequest':
            valid = response.json()['valid']
            res['msg'] = "The request is "
            res['msg'] += "valid!" if valid else "not valid!"
        elif analysis_operation == 'isDeadParameter':
            dead_parameter = response.json()['deadParameter']
            res['msg'] = "The parameter analyzed is "
            res['msg'] += "a dead parameter!" if dead_parameter else "not a dead parameter!"
        elif analysis_operation == 'isConsistent':
            consistent = response.json()['consistent']
            res['msg'] = "The specification is "
            res['msg'] += "consistent!" if consistent else "not consistent!"
        elif analysis_operation == 'isFalseOptional':
            false_optional = response.json()['falseOptional']
            res['msg'] = "The parameter analyzed is "
            res['msg'] += "a false optional!" if false_optional else "not a false optional!"
        else:
            res['msg'] = "The random request generated is the next:"
            request = operation_path + "?"
            for (key, value) in response.json().items():
                request += key + '=' + str(value) + '&'
            request = request[:-1]
            res['req'] = request
        res['err'] = False
        return res
