from django import forms
from django.conf import settings
from django.forms import CheckboxInput
from django.shortcuts import get_object_or_404

from accounts.models import User
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from topics.models import Topics
from .models import ClubMeetings
from django.utils.translation import ugettext_lazy as _


class ClubMeetingForm(forms.ModelForm):
    class_room = forms.CharField(error_messages={'required': 'Class room is required.'})
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    presence_guide_teacher = forms.BooleanField(required=False)
    presence_skleader = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}))
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': 'Select at least one topic.'})
    attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'checked': 'checked'}),
        queryset=None,
        required=True, error_messages={'required': 'Member attendance is required.'})
    date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), error_messages={'required': 'Date is required.'})
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model= ClubMeetings
        fields=["date", "class_room", "presence_guide_teacher", "image", "topics", "presence_skleader", "attendance", 'image_base64']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ClubMeetingForm, self).__init__(*args, **kwargs)
        try:
            if user.is_authenticated and user.user_type == 5:
                h_profile = SkLeaderProfile.objects.get(user=user)
            elif user.is_authenticated and user.user_type == 2 or user.user_type == 3 or user.user_type == 4:
                h_profile = HeadmasterProfile.objects.get(user=user)
        except HeadmasterProfile.DoesNotExist:
            h_profile = None

        if h_profile is not None:
            school_profile = get_object_or_404(School, pk=h_profile.school.id)
        else:
            school_profile = None

        sk_profile = SkMemberProfile.objects.filter(school__id=school_profile.id, user__user_type=6)
        u_profile = User.objects.filter(skmember_profile__in=sk_profile)
        self.fields['attendance'].queryset = u_profile

class EditClubMeetingForm(forms.ModelForm):
    presence_guide_teacher = forms.BooleanField()
    presence_skleader = forms.BooleanField()
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=False)
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=User.objects.filter(user_type=6),
        required=False)
    date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model= ClubMeetings
        fields=["date", "class_room", "presence_guide_teacher", "image", "topics", "presence_skleader", "attendance", 'image_base64']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EditClubMeetingForm, self).__init__(*args, **kwargs)
        try:
            if user.is_authenticated and user.user_type == 5:
                h_profile = SkLeaderProfile.objects.get(user=user)
            elif user.is_authenticated and user.user_type == 2 or user.user_type == 3 or user.user_type == 4:
                h_profile = HeadmasterProfile.objects.get(user=user)
        except HeadmasterProfile.DoesNotExist:
            h_profile = None
        if h_profile is not None:
            school_profile = get_object_or_404(School, pk=h_profile.school.id)
        else:
            school_profile = None
        prev_member = ClubMeetings.attendance.through.objects.filter(clubmeetings_id=self.instance)
        sk_profile = SkMemberProfile.objects.filter(school__id=school_profile.id, user__user_type=6)
        # prev_sk = (prev_member | sk_profile).distinct()
        u_profile = User.objects.filter(skmember_profile__in=sk_profile)
        # self.fields['attendance'].queryset = prev_member
        # self.fields['attendance'].queryset = u_profile
# class MeetingTopicsForm(forms.ModelForm):
#     topics = forms.ModelMultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         queryset=Topics.objects.all(),
#         required=True)
#     class Meta:
#         model= MeetingTopics
#         fields=["topics"]