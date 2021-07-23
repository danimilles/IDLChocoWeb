from django import forms
from django.core.validators import RegexValidator


class IDLForm(forms.Form):
    my_validator = RegexValidator(r"^/(.+)$", "Must begin with /")
    specification_types = [('oas', 'Open Api')]
    operation_types = [('PUT', 'Put'), ('POST', 'Post'), ('PATCH', 'Path'), ('OPTIONS', 'Options'),
                       ('HEAD', 'Head'), ('DELETE', 'Delete'), ('GET', 'Get')]
    analysis_types = [('isValidSpecification', 'IsValidSpecification'), ('isConsistent', 'IsConsistent'),
                      ('isFalseOptional', 'IsFalseOptional'), ('isDeadParameter', 'IsDeadParameter'),
                      ('generateRandomValidRequest', 'GetRandomValidRequest'),
                      ('generateRandomInvalidRequest', 'GetRandomInvalidRequest'),
                      ('isValidRequest', 'IsValidRequest'), ('isValidPartialRequest', 'IsValidPartialRequest')]
    specification_type = forms.ChoiceField(choices=specification_types, label='Specification Type',
                                           initial=('oas', 'Open Api'))
    operation_path = forms.CharField(required=True, label='Operation Path', validators=[my_validator], widget=forms.TextInput(attrs={'placeholder': '/operation/path'}))
    operation_type = forms.ChoiceField(choices=operation_types, label='Operation Types', initial=('GET', 'get'))
    analysis_operation = forms.ChoiceField(choices=analysis_types, label='Analysis Operation',
                                           initial=('isConsistent', 'IsConsistent'))
    request = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'p1=value1&p2=value2...'}), required=False, label='Request to analyze')
    parameter = forms.CharField(required=False, label='Parameter to analyze')
    api_specification = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 15}),
                                        label='API Specification (YAML/JSON or URL to YAML/JSON)')
