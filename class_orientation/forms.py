from django import forms

from topics.models import Topics
from .models import PeerEducation, place_choice


class PeerEducationForm(forms.ModelForm):
    topic = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': 'Select at least one topic.'})
    place = forms.ChoiceField(error_messages={'required': 'Place is required.'}, choices=place_choice,
                                  widget=forms.RadioSelect(attrs={'class': 'radio'}))
    created_date = forms.DateField(label='Date',error_messages={'required': 'Date is required.'}, widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = PeerEducation
        fields = ['created_date', 'place', 'topic']
