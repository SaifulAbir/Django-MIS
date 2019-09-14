from django import forms
from .models import Union





class UnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = ['division','district','upazilla','name']
