from django import forms
from .models import ClubMeetings

class ClubMeetingForms(forms.ModelForm):
    class Meta:
        model= ClubMeetings
        fields=["date","class_room","topics","attendance","image"]