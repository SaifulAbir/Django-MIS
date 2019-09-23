from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_login_required
from accounts.models import User
from headmasters import models
from headmasters.forms import UserForm, HeadmasterProfileForm, EditUserForm, HeadmasterDetailsForm
from headmasters.models import HeadmasterProfile, HeadmasterDetails
from school.models import School
import time

def headmaster_profile_view(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        #headmaster_form_details = HeadmasterProfileForm(request.POST, prefix='hf')
        profile_form = HeadmasterProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            headmaster_details = HeadmasterDetails()
            headmaster_details.school = profile_form.cleaned_data["school"]
            headmaster_details.headmaster = profile
            headmaster_details.from_date = profile_form.cleaned_data["joining_date"]
            headmaster_details.save()
            return HttpResponseRedirect("/headmasters/headmaster_list/")

    else:
        user_form = UserForm(prefix='UF')
        profile_form = HeadmasterProfileForm(prefix='PF')
        headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'headmasters/headmaster_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        #'headmaster_form_details': headmaster_form_details,
    })

#@method_decorator(headmaster_login_required, name='dispatch')
class HeadmasterList(generic.ListView):
    login_url = '/'
    model = models.HeadmasterProfile

    def get_queryset(self):
        queryset = HeadmasterProfile.objects.filter(user__user_type__in=[2,3,4])
        return queryset

class HeadmasterDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "headmaster_detail"
    model = models.HeadmasterProfile
    template_name = 'headmasters/headmaster_detail.html'

@login_required
def headmaster_update(request, pk):
    headmaster_details = HeadmasterDetails.objects.filter(headmaster=pk)
    school_list = School.objects.all()

    headmaster_profile = get_object_or_404(HeadmasterProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(headmaster_profile.user.id))
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile)
        profile_form = HeadmasterProfileForm(request.POST, request.FILES, instance=headmaster_profile)
        if user_form.is_valid() and profile_form.is_valid():
            old_password = headmaster_profile.user.password
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
            return HttpResponseRedirect("/headmasters/headmaster_list/")
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = HeadmasterProfileForm(instance=headmaster_profile)

    return render(request, 'headmasters/headmaster_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'headmaster_profile': headmaster_profile,
        'headmaster_details': headmaster_details,
        'school_list': school_list,
        'pk': pk,
    })

def headermaster_school_details_update(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    headmaster_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")

    HeadmasterDetails.objects.filter(headmaster = headmaster_id).delete()
    for school in school_list:
        heademasterModel = HeadmasterDetails()
        heademasterModel.headmaster_id = headmaster_id
        heademasterModel.school_id = school
        schoolindex = school_list.index(school)
        heademasterModel.from_date = from_date[schoolindex]

        if to_date[schoolindex] :
            heademasterModel.to_date = to_date[schoolindex]
        print(to_date[schoolindex])

        heademasterModel.save()
    time.sleep(2.5)
    return HttpResponse('ok')
