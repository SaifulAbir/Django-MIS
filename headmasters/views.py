from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import generic

from headmasters import models
from headmasters.forms import UserForm, HeadmasterProfileForm


def headmaster_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = HeadmasterProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            user.headmaster_profile.mobile = profile_form.cleaned_data.get('mobile')
            user.headmaster_profile.image = profile_form.cleaned_data.get('image')
            user.headmaster_profile.save()

    else:
        user_form = UserForm(prefix='UF')
        profile_form = HeadmasterProfileForm(prefix='PF')

    return render(request, 'headmasters/headmaster_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class HeadmasterList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.HeadmasterProfile
