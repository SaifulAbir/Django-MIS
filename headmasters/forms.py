from django import forms
from accounts.models import User
from .models import HeadmasterProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'inline-block'}))
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'user_type')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")

        return cleaned_data


class HeadmasterProfileForm(forms.ModelForm):
    class Meta:
        model = HeadmasterProfile
        fields = ('mobile','school')
