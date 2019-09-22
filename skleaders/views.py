from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
import time
# Create your views here.
from django.views import generic

from accounts.models import User
from school.models import School
from skleaders import models
from skleaders.forms import SkUserForm, SkLeaderProfileForm, EditSkUserForm
from skleaders.models import SkLeaderProfile, SkleaderDetails


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

class SkleaderDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "skleader_detail"
    model = models.SkLeaderProfile
    template_name = 'skleaders/skleader_detail.html'

def skleader_update(request, pk):
    skleader_profile = get_object_or_404(SkLeaderProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(skleader_profile.user.id))
    skleader_details = SkleaderDetails.objects.filter(skleader=pk)
    school_list = School.objects.all()

    if request.method == 'POST':
        user_form = EditSkUserForm(request.POST, instance=user_profile)
        profile_form = SkLeaderProfileForm(request.POST, request.FILES, instance=skleader_profile)
        if user_form.is_valid() and profile_form.is_valid():
            old_password = skleader_profile.user.password
            user = user_form.save(commit=False)
            form_password = user_form.cleaned_data["password"]
            if form_password:
                user.set_password(user_form.cleaned_data["password"])
            else:
                user.password = old_password
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect("/skleaders/skleader_list/")
    else:
        user_form = EditSkUserForm(instance=user_profile)
        profile_form = SkLeaderProfileForm(instance=skleader_profile)

    return render(request, 'skleaders/skleader_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skleader_profile': skleader_profile,
        'pk': pk,
        'skleader_details': skleader_details,
        'school_list': school_list,
    })

def skleader_details_update(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    headmaster_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")

    SkleaderDetails.objects.filter(skLeader = headmaster_id).delete()
    for school in school_list:
        heademasterModel = SkleaderDetails()
        heademasterModel.headmaster_id = headmaster_id
        heademasterModel.school_id = school
        schoolindex = school_list.index(school)
        heademasterModel.to_date = to_date[schoolindex]
        heademasterModel.from_date = from_date[schoolindex]
        heademasterModel.save()
    time.sleep(2.5)
    return HttpResponse('ok')

