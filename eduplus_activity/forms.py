from django import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from eduplus_activity.models import EduPlusActivity, Method
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from . import strings as edu_strings
from topics.models import Topics


class EduPlusActivityForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    presence_skleader = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}))
    description = forms.CharField(error_messages={'required': edu_strings.DESCRIPTION_REQUIRED_ERROR}, widget=forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}))
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': edu_strings.TOPIC_REQUIRED_ERROR_NOTIFICATION})
    method = forms.ModelChoiceField(
        widget=forms.Select(attrs={'width': '5000px'}),
        queryset = Method.objects.all(),
        required=True, error_messages={'required': edu_strings.METHOD_REQUIRED_ERROR_VALIDATION}
    )
    student_attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'checked': 'checked'}),
        queryset=None,
        required=True, error_messages={'required': edu_strings.ATTENDANCE_REQUIRED_ERROR})
    date = forms.DateField(label=edu_strings.DATE_LABEL_TEXT,widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), error_messages={'required': edu_strings.DATE_REQUIRED_ERROR})
    image = forms.ImageField(required=False,
                             error_messages={'invalid': _(edu_strings.IMAGE_REQUIRED_ERROR)}, widget=forms.FileInput)
    class Meta:
        model= EduPlusActivity
        fields=["date", "image", "topics", "presence_skleader",'method', "student_attendance", 'image_base64', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EduPlusActivityForm, self).__init__(*args, **kwargs)
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

        sk_profile = SkMemberProfile.objects.filter(school__id=school_profile.id)
        # u_profile = User.objects.filter(skmember_profile__in=sk_profile)
        self.fields['student_attendance'].queryset = sk_profile

class EditEduPlusActivityForm(forms.ModelForm):
    presence_skleader = forms.BooleanField()
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': edu_strings.TOPIC_REQUIRED_ERROR_NOTIFICATION})
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    description = forms.CharField(error_messages={'required': edu_strings.DESCRIPTION_REQUIRED_ERROR},
                                  widget=forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}))
    student_attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=SkMemberProfile.objects.all(),
        required=False)
    date = forms.DateField(widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',))
    image = forms.ImageField( required=False,
                             error_messages={'invalid': _(edu_strings.IMAGE_REQUIRED_ERROR)}, widget=forms.FileInput)
    class Meta:
        model= EduPlusActivity
        fields=["date", "description", "image", "topics","method", "presence_skleader", "student_attendance", 'image_base64']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(EditEduPlusActivityForm, self).__init__(*args, **kwargs)
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
        # prev_member = EduPlusActivity.attendance.through.objects.filter(eduplusactivity_id=self.instance)
        sk_profile = SkMemberProfile.objects.filter(school__id=school_profile.id)
        # prev_sk = (prev_member | sk_profile).distinct()
        #u_profile = User.objects.filter(skmember_profile__in=sk_profile)
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

class MethodForm(forms.ModelForm):
    class Meta:
        model = Method
        fields = ['name']
        widgets = {
            'name': forms.TextInput(),
        }