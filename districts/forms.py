from django import forms

from resources import strings
from .models import District


"""class DistrictForm(forms.ModelForm):
    division = forms.ModelChoiceField(queryset = Division.objects.all())
    division.widget.attrs.update({'class': 'form-control'})
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = District
        fields = ['division', 'name']"""


class DistrictForm(forms.ModelForm):
    name = forms.CharField(label=strings.DISTRICT_NAME)
    class Meta:
        model = District
        fields = ['division', 'name']
        widgets = {
            'name': forms.TextInput(
                attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
                       'style': ''}),
        }