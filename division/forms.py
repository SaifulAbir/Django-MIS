from django import forms
import division.strings as division_strings
from .models import Division

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': "[a-zA-Z\s]+", 'oninvalid': division_strings.DIVISION_NAME_VALIDATION_ERROR,}),
        }