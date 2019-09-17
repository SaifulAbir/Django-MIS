from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic

from skleaders import models
from skleaders.forms import SkUserForm, SkLeaderProfileForm
from skleaders.models import SkLeaderProfile


def skleader_profile_view(request):
    if request.method == 'POST':
        user_form = SkUserForm(request.POST, prefix='UF')
        profile_form = SkLeaderProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 5
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect("/skleaders/skleader_list/")

    else:
        user_form = SkUserForm(prefix='UF')
        profile_form = SkLeaderProfileForm(prefix='PF')

    return render(request, 'skleaders/skleader_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class SkleaderList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkLeaderProfile

    def get_queryset(self):
        queryset = SkLeaderProfile.objects.filter(user__user_type__in=[5,])
        return queryset
