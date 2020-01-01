from django import forms

from resources import strings
from . import strings as district_strings
from .models import District


class DistrictForm(forms.ModelForm):
    name = forms.CharField(label=strings.DISTRICT_NAME)
    class Meta:
        model = District
        fields = ['division', 'name']
