from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from accounts.models import User
from skmembers import models
from skmembers.forms import SkMemberUserForm, SkMemberProfileForm, EditSkMemberUserForm
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
            messages.success(request, 'SkMember Created!')
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
    
def skmember_update(request, pk):
    skmember_profile = get_object_or_404(SkMemberProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(skmember_profile.user.id))
    if request.method == 'POST':
        user_form = EditSkMemberUserForm(request.POST, instance=user_profile)
        profile_form = SkMemberProfileForm(request.POST, request.FILES, instance=skmember_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, 'SkMember Updated!')
            return HttpResponseRedirect("/skmembers/skmember_list/")
    else:
        user_form = EditSkMemberUserForm(instance=user_profile)
        profile_form = SkMemberProfileForm(instance=skmember_profile)

    return render(request, 'skmembers/skmember_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skmember_profile': skmember_profile,
    })

class SkMemberDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "skmember_detail"
    model = models.SkMemberProfile
    template_name = 'skmembers/skmember_detail.html'
