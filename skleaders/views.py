from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
import time
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import admin_login_required
from accounts.models import User
from school.models import School
from skleaders import models
from skleaders.forms import SkUserForm, SkLeaderProfileForm, EditSkUserForm, EditSkLeaderProfileForm
from skleaders.models import SkLeaderProfile, SkleaderDetails
from datetime import datetime

@admin_login_required
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

            headmaster_details = SkleaderDetails()
            headmaster_details.school = profile_form.cleaned_data["school"]
            headmaster_details.skleader = profile
            headmaster_details.from_date = profile_form.cleaned_data["joining_date"]
            headmaster_details.save()
            messages.success(request, 'SK Leader Created!')

            return HttpResponseRedirect("/skleaders/skleader_list/")

    else:
        user_form = SkUserForm(prefix='UF')
        profile_form = SkLeaderProfileForm(prefix='PF')

    return render(request, 'skleaders/skleader_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def skleader_list(request):
    qs=SkLeaderProfile.objects.filter(user__user_type__in=[5])
    name= request.GET.get('name_contains')
    school= request.GET.get('school_contains')

    if name !='' and name is not None:
        qs = qs.filter(user__first_name__icontains=name)
    if school != '' and school is not None:
        qs = qs.filter(school__name__icontains=school)
    return render(request, 'skleaders/skleaderprofile_list.html', {'queryset': qs, 'name': name, 'school':school})

@method_decorator(admin_login_required, name='dispatch')
class SkleaderDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "skleader_detail"
    model = models.SkLeaderProfile
    template_name = 'skleaders/skleader_detail.html'

@admin_login_required
def skleader_update(request, pk):
    skleader_profile = get_object_or_404(SkLeaderProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(skleader_profile.user.id))
    skleader_details = SkleaderDetails.objects.filter(skleader=pk)
    school_list = School.objects.all()

    if request.method == 'POST':
        user_form = EditSkUserForm(request.POST, instance=user_profile)
        profile_form = EditSkLeaderProfileForm(request.POST, request.FILES, instance=skleader_profile)
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
            messages.success(request, 'SK Leader Updated!')
            return HttpResponseRedirect("/skleaders/skleader_list/")
    else:
        user_form = EditSkUserForm(instance=user_profile)
        profile_form = EditSkLeaderProfileForm(instance=skleader_profile)

    return render(request, 'skleaders/skleader_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skleader_profile': skleader_profile,
        'pk': pk,
        'skleader_details': skleader_details,
        'school_list': school_list,
    })

@admin_login_required
def skleader_details_update(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    skleader_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")

    SkleaderDetails.objects.filter(skleader = skleader_id).delete()
    current_school_index = len(school_list)
    for school in school_list:
        skleaderModel = SkleaderDetails()
        skleaderModel.skleader_id = skleader_id
        skleaderModel.school_id = school
        schoolindex = school_list.index(school)
        fromdate = datetime.strptime(from_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')

        skleaderModel.from_date = fromdate
        if schoolindex == current_school_index-1:
            skleader_obj=SkLeaderProfile.objects.get(pk=skleader_id)
            skleader_obj.school_id = school
            skleader_obj.save()

        if to_date[schoolindex]:
            todate = datetime.strptime(to_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')
            skleaderModel.to_date = todate
        skleaderModel.save()
    time.sleep(1)
    return HttpResponse('ok')

