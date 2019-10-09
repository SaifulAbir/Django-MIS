from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import admin_login_required
from accounts.models import User
from skleaders.models import SkLeaderProfile
from skmembers import models
from skmembers.forms import SkMemberUserForm, SkMemberProfileForm, EditSkMemberUserForm, SkMemberProfileFormForSkleader
from skmembers.models import SkMemberProfile

@admin_login_required
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
            messages.success(request, 'SK Member Created!')
            return HttpResponseRedirect("/skmembers/skmember_list/")

    else:
        user_form = SkMemberUserForm(prefix='UF')
        profile_form = SkMemberProfileForm(prefix='PF')

    return render(request, 'skmembers/skmember_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def skmember_profile_view_skleader(request):
    if request.method == 'POST':
        user_form = SkMemberUserForm(request.POST, prefix='UF')
        profile_form = SkMemberProfileFormForSkleader(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            id = request.user.id
            objSkLeader = SkLeaderProfile.objects.get(user_id=id)
            school_id = objSkLeader.school_id

            user = user_form.save(commit=False)
            user.user_type = 6
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.school_id = school_id
            profile.save()
            return HttpResponseRedirect("/skmembers/skmember_list_for_skleader/")
    else:
        user_form = SkMemberUserForm(prefix='UF')
        profile_form = SkMemberProfileFormForSkleader(prefix='PF')

    return render(request, 'skmembers/skmember_profile_add_for_skleader.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def skmember_update_for_skleader(request, pk):
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
            return HttpResponseRedirect("/skmembers/skmember_list_for_skleader/")
    else:
        user_form = EditSkMemberUserForm(instance=user_profile)
        profile_form = SkMemberProfileForm(instance=skmember_profile)

    return render(request, 'skmembers/skmember_profile_add_for_skleader.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skmember_profile': skmember_profile,
    })

@method_decorator(admin_login_required, name='dispatch')
class SkmemberList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile
    def get_queryset(self):
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,])
        return queryset
    
class SkmemberListforSkLeader(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile
    template_name = 'skmembers/skmemberprofile_list_for_skleader.html'


    def get_queryset(self):
        loggedinuser = self.request.user.id
        objSkLeader = SkLeaderProfile.objects.get(user_id=loggedinuser)
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,],school_id=objSkLeader.school_id)

        return queryset

class SkmemberListForSkmber(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile

    def get_queryset(self):
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,])
        return queryset

@admin_login_required
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
            messages.success(request, 'SK Member Updated!')
            return HttpResponseRedirect("/skmembers/skmember_list/")
    else:
        user_form = EditSkMemberUserForm(instance=user_profile)
        profile_form = SkMemberProfileForm(instance=skmember_profile)

    return render(request, 'skmembers/skmember_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skmember_profile': skmember_profile,
    })

@method_decorator(admin_login_required, name='dispatch')
class SkMemberDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "skmember_detail"
    model = models.SkMemberProfile
    template_name = 'skmembers/skmember_detail.html'
