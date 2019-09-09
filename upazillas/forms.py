from django import forms

from upazillas.models import Upazilla


class UpazillaForm(forms.ModelForm):
    class Meta:
        model = Upazilla
        fields = ['division', 'district', 'name']
        widgets = {
            'name': forms.TextInput(
                attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
                       'style': ''}),
        }
