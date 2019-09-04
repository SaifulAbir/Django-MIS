from django import forms
from .models import Division




class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = ['name']