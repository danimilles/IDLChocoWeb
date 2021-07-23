from django import forms
from django.core.validators import RegexValidator


class IDLForm(forms.Form):
    my_validator = RegexValidator(r"^/(.+)$", "Must begin with /")
    specification_types = [('oas', 'Open Api')]
    operation_types = [('PUT', 'Put'), ('POST', 'Post'), ('PATCH', 'Path'), ('OPTIONS', 'Options'),
                       ('HEAD', 'Head'), ('DELETE', 'Delete'), ('GET', 'Get')]
    analysis_types = [('isValidSpecification', 'IsValidSpecification'), ('isConsistent', 'IsConsistent'),
                      ('isFalseOptional', 'IsFalseOptional'), ('isDeadParameter', 'IsDeadParameter'),
                      ('getRandomValidRequest', 'GetRandomValidRequest'),
                      ('getRandomInvalidRequest', 'GetRandomInvalidRequest'),
                      ('isValidRequest', 'IsValidRequest'), ('isValidPartialRequest', 'IsValidPartialRequest')]
    specification_type = forms.ChoiceField(choices=specification_types, label='Specification Type',
                                           initial=('oas', 'Open Api'))
    operation_path = forms.CharField(required=True, label='Operation Path', validators=[my_validator])
    operation_type = forms.ChoiceField(choices=operation_types, label='Opertaion Types', initial=('PUT', 'Put'))
    analysis_operation = forms.ChoiceField(choices=analysis_types, label='Analysis Operation',
                                           initial=('isConsistent', 'IsConsistent'))
    request = forms.CharField(widget=forms.TextInput, required=False, label='Request to analyze')
    parameter = forms.CharField(required=False, label='Parameter to analyze')
    api_specification = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 15}),
                                        label='API Specification (YAML/JSON or URL to YAML/JSON)')
