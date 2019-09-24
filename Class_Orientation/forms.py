from django import forms
from .models import Class_Orientation


"""class DistrictForm(forms.ModelForm):
    division = forms.ModelChoiceField(queryset = Division.objects.all())
    division.widget.attrs.update({'class': 'form-control'})
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = District
        fields = ['division', 'name']"""


class Class_OrientationForm(forms.ModelForm):
    class Meta:
        model = Class_Orientation
        fields = ['topic', 'class_name']
        widgets = {
            'topic': forms.TextInput(
                attrs={'pattern': '[a-zA-Z\s]+', 'oninvalid': "setCustomValidity('Please enter on alphabets only. ')",
                       'style': ''}),
        }