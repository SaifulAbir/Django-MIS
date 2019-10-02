from django import forms
from .models import Division

class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')", 'style': ''}),
        }