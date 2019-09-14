from django import forms
from .models import Union





class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ['division','district','upazilla','name']
<<<<<<< HEAD
=======
        # widgets = {
        #     'name': forms.TextInput(
        #         attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
        #                'style': ''}),
        # }
>>>>>>> 037e5151cc100c6a2f3fb4b1cd358e6cd44bdc95
