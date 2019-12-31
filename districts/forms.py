from django import forms

from resources import strings
from . import strings as district_strings
from .models import District


class DistrictForm(forms.ModelForm):
    name = forms.CharField(label=strings.DISTRICT_NAME)
    class Meta:
        model = District
        fields = ['division', 'name']
        widgets = {
            'name': forms.TextInput(
                attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': district_strings.DISTRICT_NAME_VALIDATION_ERROR,}),
        }