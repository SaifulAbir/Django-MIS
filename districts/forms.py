from django import forms
from .models import District


"""class DistrictForm(forms.ModelForm):
    division = forms.ModelChoiceField(queryset = Division.objects.all())
    division.widget.attrs.update({'class': 'form-control'})
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = District
        fields = ['division', 'name']"""


class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['division', 'name']