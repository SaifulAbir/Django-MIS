from django import forms
from .models import Union



class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ['division','district','upazilla','name']
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
        #                'style': ''}),
        # }
