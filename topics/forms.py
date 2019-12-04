from django import forms
from .models import Topics




class TopicsForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'style': ''}),
        }