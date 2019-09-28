from django import forms
from django.template import Template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from skleaders.models import SkLeaderProfile
from django.utils.translation import ugettext_lazy as _




class SkUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, 'skLeader'),
        (6, 'skMember'),
    )

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type',)

    def clean(self):
        cleaned_data = super(SkUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data

class EditSkUserForm(forms.ModelForm):

    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput())
    user_type = forms.ChoiceField(required=False, choices=SkUserForm.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'radio'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(EditSkUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


class SkLeaderProfileForm(forms.ModelForm):

    image = forms.ImageField(label=_('Skleader image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll', 'school','joining_date')

class EditSkLeaderProfileForm(forms.ModelForm):

    image = forms.ImageField(label=_('Skleader image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    joining_date = forms.DateField(required=False)
    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll','joining_date')