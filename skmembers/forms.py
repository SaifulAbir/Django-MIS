from django import forms
from accounts.models import User
from skmembers.models import SkMemberProfile
from django.utils.translation import ugettext_lazy as _


class SkMemberUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, 'skLeader'),
        (6, 'skMember'),
    )

    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'user_type',)

class EditSkMemberUserForm(forms.ModelForm):

    user_type = forms.ChoiceField(required=False, choices=SkMemberUserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))

    class Meta:
        model = User
        fields = ('first_name', 'email', 'user_type')



class SkMemberProfileForm(forms.ModelForm):
    image = forms.ImageField(label=_('SkMember image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll', 'school')