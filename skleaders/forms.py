from django import forms
from django.core.exceptions import ValidationError
from django.template import Template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from accounts.models import User
from school.models import School
from skleaders.models import SkLeaderProfile
from django.utils.translation import ugettext_lazy as _




class SkUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, 'skLeader'),
        (6, 'skMember'),
    )

    class_choice = (

        ('', '--Select--'),

        ('6', '6'),

        ('7', '7'),

        ('8', '8'),

        ('9', '9'),

        ("10", '10'),)

    email = forms.EmailField(error_messages={'required': 'Email is required.'})

    password = forms.CharField(error_messages={'required': 'Password is required.'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    confirm_password = forms.CharField(error_messages={'required': 'Confirm password is required.'},
                                       widget=forms.PasswordInput())
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
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
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
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})

    joining_date = forms.DateField(error_messages={'required': 'From date is required.'})

    roll = forms.CharField(error_messages={'required': 'Roll is required.'})

    student_class = forms.ChoiceField(error_messages={'required': 'Class is required.'},
                                      choices=SkUserForm.class_choice, widget=forms.Select())
    image = forms.ImageField(label=_('Skleader image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    school = forms.ModelChoiceField(error_messages={'required': 'School is required.'}, queryset=School.objects.all())

    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll', 'school','joining_date','emergency_contact_person','emergency_contact_number')

    def clean_image(self):

        image = self.cleaned_data.get('image', False)

        if image:

            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")

            return image

class EditSkLeaderProfileForm(forms.ModelForm):
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})

    joining_date = forms.DateField(error_messages={'required': 'From date is required.'})

    roll = forms.CharField(error_messages={'required': 'Roll is required.'})

    student_class = forms.ChoiceField(error_messages={'required': 'Class is required.'},
                                      choices=SkUserForm.class_choice, widget=forms.Select())

    image = forms.ImageField(label=_('Skleader image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)

    joining_date = forms.DateField(required=False)
    class Meta:
        model = SkLeaderProfile
        fields = ('mobile', 'image', 'student_class', 'roll','joining_date', 'emergency_contact_person','emergency_contact_number')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image