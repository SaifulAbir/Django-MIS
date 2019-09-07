from django import forms

from upazillas.models import Upazilla


class UpazillaForm(forms.ModelForm):
    class Meta:
        model = Upazilla
        fields = ['division', 'district', 'name']
