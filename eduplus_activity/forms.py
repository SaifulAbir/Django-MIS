from django import forms
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from eduplus_activity.models import EduPlusActivity
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from topics.models import Topics


class EduPlusActivityForm(forms.ModelForm):
    image_base64 = forms.CharField(required=False, widget=forms.HiddenInput())
    presence_skleader = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}))
    description = forms.CharField(error_messages={'required': 'Description is required.'}, widget=forms.Textarea(attrs={'rows': 4.5, 'cols': 15, 'style': 'height:7.51em;'}))
    topics = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Topics.objects.all(),
        required=True, error_messages={'required': 'Select at least one topic.'})
    attendance = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(attrs={'checked': 'checked'}),
        queryset=None,
        required=True, error_messages={'required': 'Member attendance is required.'})
    date = forms.DateField(label='dd-mm-yyyy',widget=forms.DateInput(format = '%d-%m-%Y'), input_formats=('%d-%m-%Y',), error_messages={'required': 'Date is required.'})
    image = forms.ImageField(label=_('Headmaster image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    class Meta:
        model= EduPlusActivity
        fields=["date", "image", "topics", "presence_skleader", "attendance", 'image_base64', 'description']
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

        sk_profile = SkMemberProfile.objects.filter(school__id=school_profile.id, user__user_type=6)
        u_profile = User.objects.filter(skmember_profile__in=sk_profile)
        self.fields['attendance'].queryset = u_profile