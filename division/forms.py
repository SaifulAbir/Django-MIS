from django import forms

from resources import strings
from .models import Division

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': strings.DIVISION_NAME_VALIDATION_PATTERN, 'oninvalid': strings.DIVISION_NAME_VALIDATION_ERROR,}),
        }