from PIL import Image
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from . import strings as headmaster_strings
from resources import strings as common_strings
# Create your views here.
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import admin_login_required
from accounts.models import User
from headmasters import models
from headmasters.forms import UserForm, HeadmasterProfileForm, EditUserForm, HeadmasterDetailsForm
from headmasters.models import HeadmasterProfile, HeadmasterDetails
from school.models import School
import time
from datetime import datetime
import base64, uuid
from django.core.files.base import ContentFile
from headmasters.resources import HeadmasterResource
from django.core.files.storage import FileSystemStorage

@admin_login_required
def headmaster_profile_view(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, prefix='UF')
        profile_form = HeadmasterProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data["password"])
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user

            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-headmaster.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/'+filename
            # end of image cropping code

            profile.save()
            user.username = profile.mobile
            user.save()
            headmaster_details = HeadmasterDetails()
            headmaster_details.school = profile_form.cleaned_data["school"]
            headmaster_details.headmaster = profile
            headmaster_details.from_date = profile_form.cleaned_data["joining_date"]
            headmaster_details.save()
            messages.success(request, 'Headmaster Created!')
            return HttpResponseRedirect("/headmasters/headmaster_list/")

    else:
        user_form = UserForm(prefix='UF')
        profile_form = HeadmasterProfileForm(prefix='PF')
        headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'headmasters/headmaster_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'headmaster_strings': headmaster_strings,
        'common_strings':common_strings
        #'headmaster_form_details': headmaster_form_details,
    })


@method_decorator(admin_login_required, name='dispatch')
class HeadmasterDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "headmaster_detail"
    model = models.HeadmasterProfile
    template_name = 'headmasters/headmaster_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["headmaster_strings"] = headmaster_strings
        context["common_strings"] = common_strings
        return context


@admin_login_required
def headmaster_list(request, export='null'):
    qs=HeadmasterProfile.objects.filter(user__user_type__in=[2,3,4])
    name= request.GET.get('name_contains')
    school= request.GET.get('school_contains')
    if name !='' and name is not None:
        qs = qs.filter(user__first_name__icontains=name)
    if school != '' and school is not None:
        qs = qs.filter(school__name__icontains=school)
    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if export != 'export':
        return render(request, 'headmasters/headmasterprofile_list.html',
                      {'queryset': queryset, 'name': name, 'school': school,'headmaster_strings':headmaster_strings,'common_strings':common_strings})
    else:
        resource = HeadmasterResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="headmaster_list.csv"'
        return response


@admin_login_required
def headmaster_update(request, pk):
    headmaster_details = HeadmasterDetails.objects.filter(headmaster=pk)
    school_list = School.objects.all()

    headmaster_profile = get_object_or_404(HeadmasterProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(headmaster_profile.user.id))
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile)
        profile_form = HeadmasterProfileForm(request.POST, request.FILES, instance=headmaster_profile, prefix='PF')
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
            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-headmaster.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/' + filename
            # end of image cropping code
            profile.save()
            user.username = profile.mobile
            user.save()
            messages.success(request, 'Headmaster Updated!')
            return HttpResponseRedirect("/headmasters/headmaster_list/")
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = HeadmasterProfileForm(instance=headmaster_profile, prefix='PF')

    return render(request, 'headmasters/headmaster_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'headmaster_profile': headmaster_profile,
        'headmaster_details': headmaster_details,
        'school_list': school_list,
        'pk': pk,
        'headmaster_strings':headmaster_strings,
        'common_strings':common_strings
    })

@admin_login_required
def headermaster_school_details_update(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    headmaster_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")
    current_school_index = len(school_list)

    HeadmasterDetails.objects.filter(headmaster = headmaster_id).delete()
    for school in school_list:
        heademasterModel = HeadmasterDetails()
        heademasterModel.headmaster_id = headmaster_id
        heademasterModel.school_id = school
        schoolindex = school_list.index(school)

        fromdate = datetime.strptime(from_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')

        heademasterModel.from_date = fromdate

        if to_date[schoolindex]:
            todate = datetime.strptime(to_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')
            heademasterModel.to_date = todate

        if schoolindex ==current_school_index-1:
            headmaster_obj=HeadmasterProfile.objects.get(pk=headmaster_id)
            headmaster_obj.school_id = school;
            headmaster_obj.save()

        heademasterModel.save()
    time.sleep(1)
    return HttpResponse('ok')


def headmaster_search_list(request, export='null'):
    data = dict()
    qs = HeadmasterProfile.objects.filter(user__user_type__in=[2, 3, 4])
    name = request.GET.get('name_contains')
    school = request.GET.get('school_contains')

    if name != '' and name is not None:
        qs = qs.filter(user__first_name__icontains=name)
    if school != '' and school is not None:
        qs = qs.filter(school__name__icontains=school)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and school == '':
        queryset = None
    data['form_is_valid'] = True
    data['html_list'] = render_to_string('headmasters/partial_headmaster_list.html',
                                                {'queryset': queryset,'headmaster_strings':headmaster_strings,'common_strings':common_strings})

    if export != 'export':
        return JsonResponse(data)
    else:
        resource = HeadmasterResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="headmaster_list.csv"'
        return response


