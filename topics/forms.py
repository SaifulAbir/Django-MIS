from django import forms
from .models import Topics




class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')", 'style': ''}),
        }