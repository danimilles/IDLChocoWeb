import re

from django.shortcuts import render, redirect

# Create your views here.
from IDLChocoWebApp.forms import IDLForm
from IDLChocoWebApp.service import invoke_api


def index(request):
    form = IDLForm()
    if request.method == 'POST':
        form = IDLForm(data=request.POST)

        if form['analysis_operation'] == 'isFalseOptional' or form['analysis_operation'] == 'isDeadParameter':
            form.add_error('parameter', 'For this operation field Parameter is required')
        if form['analysis_operation'] == 'isValidRequest' or form['analysis_operation'] == 'isValidPartialRequest':
            form.add_error('request', 'For this operation field Request is required')
        if form.is_valid():
            if re.match(r"^http(s)?://+", form['api_specification']):
                response = invoke_api(form);
                form.clean()
            return render(request, 'index.html', {'form': form, 'response': response})
    return render(request, 'index.html', {'form': form})