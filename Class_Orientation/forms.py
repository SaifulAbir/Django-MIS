from django import forms
from .models import Class_Orientation




class Class_OrientationForm(forms.ModelForm):
    class Meta:
        model = Class_Orientation
        fields = ['name','class_no']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')", 'style': ''}),
        }