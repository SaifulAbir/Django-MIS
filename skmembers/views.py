from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import generic

from skmembers import models
from skmembers.forms import SkMemberUserForm, SkMemberProfileForm
from skmembers.models import SkMemberProfile


def skmember_profile_view(request):
    if request.method == 'POST':
        user_form = SkMemberUserForm(request.POST, prefix='UF')
        profile_form = SkMemberProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 6
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect("/skmembers/skmember_list/")

    else:
        user_form = SkMemberUserForm(prefix='UF')
        profile_form = SkMemberProfileForm(prefix='PF')

    return render(request, 'skmembers/skmember_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class SkmemberList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile

    def get_queryset(self):
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,])
        return queryset
