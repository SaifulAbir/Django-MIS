from django import forms
from accounts.models import User
from .models import HeadmasterProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class HeadmasterProfileForm(forms.ModelForm):
    class Meta:
        model = HeadmasterProfile
        fields = ('mobile','school')
