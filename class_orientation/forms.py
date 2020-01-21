from django import forms
import class_orientation.strings as class_orientation_strings
from topics.models import Topics
from .models import PeerEducation, place_choice


class PeerEducationForm(forms.ModelForm):
    topic = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': class_orientation_strings.TOPIC_REQUIRED_MSG})
    place = forms.ChoiceField(error_messages={'required': class_orientation_strings.PLACE_REQUIRED_MSG}, choices=place_choice,
                                  widget=forms.RadioSelect(attrs={'class': 'radio'}))
    created_date = forms.DateField(label=class_orientation_strings.PEER_EDUCATION_DATE_TEXT,error_messages={'required': class_orientation_strings.DATE_REQUIRED_MSG}, widget=forms.DateInput(format='%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    class Meta:
        model = PeerEducation
        fields = ['created_date', 'place', 'topic']
