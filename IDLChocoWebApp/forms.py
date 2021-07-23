from django import forms


class IDLForm(forms.Form):
    specification_types = (('oas', 'Open Api'))
    opertaion_types = (('PUT', 'Put'), ('POST', 'Post'), ('PATCH', 'Path'), ('OPTIONS', 'Options'),
                       ('HEAD', 'Head'), ('DELETE', 'Delete'), ('GET', 'Get'))
    analysis_types = (('isValidSpecification', 'IsValidSpecification'), ('isConsistent', 'IsConsistent'),
                      ('isFalseOptional', 'IsFalseOptional'), ('isDeadParameter', 'IsDeadParameter'),
                      ('getRandomValidRequest', 'GetRandomValidRequest'),
                      ('getRandomInvalidRequest', 'GetRandomInvalidRequest'),
                      ('isValidRequest', 'IsValidRequest'), ('isValidPartialRequest', 'IsValidPartialRequest'))
    specification_type = forms.ChoiceField(choices=specification_types, required=True, label='Specification Type')
    api_specification = forms.Textarea(required=True, label='API Specification (YAML or URL to YAML)')
    operation_path = forms.IntegerField(required=True, label='Página', min_value=1, initial=1)
    operation_type = forms.ChoiceField(choices=opertaion_types, required=True, label='Opertaion Types')
    analysis_operation = forms.ChoiceField(choices=analysis_types, required=True, label='Analysis Operation')
    request = forms.TextInput(choices=opertaion_types, required=False, label='Request to analyze')
    parameter = forms.TextInput(choices=opertaion_types, required=False, label='Parameter to analyze')
