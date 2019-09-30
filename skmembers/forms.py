from django import forms
from django.core.exceptions import ValidationError

from accounts.models import User
from skleaders.forms import SkUserForm
from skmembers.models import SkMemberProfile
from django.utils.translation import ugettext_lazy as _


class SkMemberUserForm(forms.ModelForm):
    USER_TYPE_CHOICES = (
        (5, 'skLeader'),
        (6, 'skMember'),
    )
    class_choice = (
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ("10", '10'),
    )
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
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
    roll = forms.CharField(error_messages={'required': 'Roll is required.'})
    student_class = forms.ChoiceField(error_messages={'required': 'Class is required.'},
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll', 'school')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

class SkMemberProfileFormSkleader(forms.ModelForm):
    image = forms.ImageField(label=_('SkMember image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    roll = forms.CharField(error_messages={'required': 'Roll is required.'})
    student_class = forms.ChoiceField(error_messages={'required': 'Class is required.'},
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image

class SkMemberProfileFormForSkleader(forms.ModelForm):
    image = forms.ImageField(label=_('SkMember image'), required=False,
                             error_messages={'invalid': _("Image files only")}, widget=forms.FileInput)
    roll = forms.CharField(error_messages={'required': 'Roll is required.'})
    student_class = forms.ChoiceField(error_messages={'required': 'Class is required.'},
                                      choices=SkMemberUserForm.class_choice, widget=forms.Select())
    mobile = forms.CharField(error_messages={'required': 'Mobile is required.'})
    class Meta:
        model = SkMemberProfile
        fields = ('mobile', 'image', 'student_class', 'roll')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 1 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 1mb )")
            return image