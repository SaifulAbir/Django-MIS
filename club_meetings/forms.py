from django import forms
from django.conf import settings
from django.forms import CheckboxInput

from accounts.models import User
from topics.models import Topics
from .models import ClubMeetings
from django.utils.translation import ugettext_lazy as _


class ClubMeetingForm(forms.ModelForm):
    presence_guide_teacher = forms.BooleanField()
    presence_skleader = forms.BooleanField()
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True)
    attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=User.objects.filter(user_type=6),
        required=True)
    date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model= ClubMeetings
        fields=["date", "class_room", "presence_guide_teacher", "image", "topics", "presence_skleader", "attendance"]

# class MeetingTopicsForm(forms.ModelForm):
#     topics = forms.ModelMultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         queryset=Topics.objects.all(),
#         required=True)
#     class Meta:
#         model= MeetingTopics
#         fields=["topics"]