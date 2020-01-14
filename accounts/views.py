import random
import accounts.strings as account_strings
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, urls, forms, views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import loader
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseForbidden, JsonResponse
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
import base64, uuid
from django.shortcuts import render, redirect
from resources import strings as common_strings


# Create your views here.
from django.template import RequestContext
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from accounts.decorators import admin_login_required
from accounts.forms import PrettyAuthenticationForm, EditUserForm, HeadmasterProfileForm, SkleaderProfileForm
from accounts.models import User
from districts.models import District
from division.models import Division
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from unions.models import Union
from upazillas.models import Upazilla


@admin_login_required
def index(request):
    data = dict()
    schools = School.objects.all()
    school_total = School.objects.count()
    headmaster_total = User.objects.filter(user_type__in=[2,]).count()
    skleader_total = User.objects.filter(user_type__in=[5,]).count()
    skmember_total = User.objects.filter(user_type__in=[6,]).count()
    paginator = Paginator(schools, 10)
    page = request.GET.get('page')
    try:
        school_list = paginator.page(page)
    except PageNotAnInteger:
        school_list = paginator.page(1)
    except EmptyPage:
        school_list = paginator.page(paginator.num_pages)
    if request.is_ajax():
        data['form_is_valid'] = True
        data['html_list'] = render_to_string('school/partial_school_list_dashboard.html',
                                             {'school_list': school_list, 'common_strings':common_strings})
        return JsonResponse(data)
    context = {'PROJECT_NAME': settings.PROJECT_NAME, 'school_list': school_list, 'common_strings':common_strings,
               'school_total': school_total, 'headmaster_total': headmaster_total, 'skleader_total': skleader_total, 'skmember_total': skmember_total}
    return render(request, 'sknf/index.html', context)


@login_required(login_url='/')
def events(request):
    return render(request, 'sknf/events.html')




def custom_login(request):
    next_destination = request.GET.get('next')
    if request.user.is_authenticated and request.user.user_type == 1:
        if next_destination:
            raise PermissionDenied
        return redirect('/dashboard/')
    elif request.user.is_authenticated and request.user.user_type == 2:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            raise PermissionDenied
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 3:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            raise PermissionDenied
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 4:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            raise PermissionDenied
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 5:
        skleader_profile = SkLeaderProfile.objects.get(user=request.user)
        if next_destination:
            raise PermissionDenied
        return redirect('school:school_profile', skleader_profile.school.id)
    else:
        return home_login(request)

@admin_login_required
def admin_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    old_user_profile = user_profile.image
    old_email = user_profile.email
    old_password = user_profile.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, files=request.FILES, instance=user_profile, prefix='PF')

        if user_form.is_valid():
            user_update = user_form.save(commit=False)
            user_update.user_type = 1
            form_password = user_form.cleaned_data["password"]
            if form_password:
                user_update.set_password(user_form.cleaned_data["password"])
            else:
                user_update.password = old_password

            update_session_auth_hash(request, user_update)

            # image cropping code start here
            img_base64 = user_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-admin.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                user_update.image.save(filename, data, save=True)
                user_update.image = 'images/' + filename
            # end of image cropping code

            user_update.save()
            update_session_auth_hash(request, user_update)
            return redirect("accounts:dashboard")

    else:
        user_form = EditUserForm(instance=user_profile, prefix='PF')

    return render(request, 'accounts/admin_profile_form.html', {
        'user_form': user_form,
        'user_profile': user_profile,
        'old_user_profile': old_user_profile,
        'account_strings': account_strings,
        'common_strings': common_strings
    })

@login_required(login_url='/')
def headmaster_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
    old_password = headmaster_profile.user.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile, )
        profile_form = HeadmasterProfileForm(request.POST, request.FILES, instance=headmaster_profile, prefix='PF')
        if user_form.is_valid() and profile_form.is_valid():
            user_update = user_form.save(commit=False)
            form_password = user_form.cleaned_data["password"]
            if form_password:
                user_update.set_password(user_form.cleaned_data["password"])
            else:
                user_update.password = old_password
            user_update.save()
            update_session_auth_hash(request, user_update)
            profile = profile_form.save(commit = False)
            profile.user = user_update
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
            return redirect("school:school_profile", pk= headmaster_profile.school_id)
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = HeadmasterProfileForm(instance=headmaster_profile, prefix='PF')

    return render(request, 'accounts/headmaster_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'headmaster_profile': headmaster_profile,
        'account_strings': account_strings,
        'common_strings': common_strings
    })

@login_required(login_url='/')
def skleader_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    skleader_profile = SkLeaderProfile.objects.get(user=request.user)
    old_password = skleader_profile.user.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile)
        profile_form = SkleaderProfileForm(request.POST, request.FILES, instance=skleader_profile, prefix='PF')
        if user_form.is_valid() and profile_form.is_valid():
            user_update = user_form.save(commit=False)
            form_password = user_form.cleaned_data["password"]
            if form_password:
                user_update.set_password(user_form.cleaned_data["password"])
            else:
                user_update.password = old_password
            user_update.save()
            update_session_auth_hash(request, user_update)
            profile = profile_form.save(commit = False)
            profile.user = user_update
            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-skleader.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/' + filename
            # end of image cropping code
            profile.save()
            return redirect("school:school_profile", pk= skleader_profile.school_id)
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = SkleaderProfileForm(instance=skleader_profile, prefix='PF')

    return render(request, 'accounts/skleader_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skleader_profile': skleader_profile,
        'account_strings': account_strings,
        'common_strings': common_strings
    })


def handler403(request, exception):
    return render(request, 'accounts/403.html', status=403)


def home_login(request):
    next_destination = request.GET.get('next')
    if request.method == 'POST':
        form = PrettyAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next_destination:
                    return redirect(next_destination)
                if user.user_type == 1:
                    return redirect('/dashboard/')
                elif user.user_type == 2:
                    headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
                    return redirect('school:school_profile', headmaster_profile.school.id)
                elif user.user_type == 3:
                    headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
                    return redirect('school:school_profile', headmaster_profile.school.id)
                elif user.user_type == 4:
                    headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
                    return redirect('school:school_profile', headmaster_profile.school.id)
                elif user.user_type == 5:
                    skleader_profile = SkLeaderProfile.objects.get(user=request.user)
                    return redirect('school:school_profile', skleader_profile.school.id)
            else:
                messages.error(request, account_strings.SIGN_IN_INVALID_ERROR)
        else:
            messages.error(request, account_strings.SIGN_IN_INVALID_ERROR)
    form = PrettyAuthenticationForm()
    data = dict()
    qs = School.objects.all()
    name = request.POST.get('name_contains')
    division = request.GET.get('division_contains')
    district = request.GET.get('district_contains')
    upazilla = request.GET.get('upazilla_contains')
    union = request.GET.get('union_contains')
    if name != '' and name is not None:
        qs = qs.filter(name__icontains=name)
    if division != '' and division is not None:
        qs = qs.filter(division__name__icontains=division)
    if district != '' and district is not None:
        qs = qs.filter(district__name__icontains=district)
    if upazilla != '' and upazilla is not None:
        qs = qs.filter(upazilla__name__icontains=upazilla)
    if union != '' and union is not None:
        qs = qs.filter(union__name__icontains=union)
    return render(request, 'accounts/home_login.html', {'name': name, 'division': division, 'district': district, 'upazilla': upazilla, 'union': union,
                                                        'form':form, 'next_destination':next_destination, 'account_strings': account_strings, 'common_strings':common_strings})

def search_school_list(request):
    data = dict()
    qs = School.objects.all()
    name = request.GET.get('name_contains')
    division = request.GET.get('division_contains')
    district = request.GET.get('district_contains')
    upazilla = request.GET.get('upazilla_contains')
    union = request.GET.get('union_contains')
    if name != '' and name is not None:
        qs = qs.filter(name__icontains=name)
    if division != '' and division is not None:
        qs = qs.filter(division__name__icontains=division)
    if district != '' and district is not None:
        qs = qs.filter(district__name__icontains=district)
    if upazilla != '' and upazilla is not None:
        qs = qs.filter(upazilla__name__icontains=upazilla)
    if union != '' and union is not None:
        qs = qs.filter(union__name__icontains=union)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and division == '' and district == '' and upazilla == '' and union == '':
        queryset = None
    data['form_is_valid'] = True
    data['html_school_list'] = render_to_string('accounts/partial_school_list.html',
                                                {'queryset': queryset, 'common_strings':common_strings, 'account_strings':account_strings})
    return JsonResponse(data)

def load_previous_school(request):
    previous_schools = list(School.objects.values_list('name', flat=True))
    return JsonResponse(previous_schools, safe=False)
def load_previous_eiin(request):
    previous_eiins = list(School.objects.values_list('school_id', flat=True))
    return JsonResponse(previous_eiins, safe=False)
def load_previous_division(request):
    previous_divisions = list(Division.objects.values_list('name', flat=True))
    return JsonResponse(previous_divisions, safe=False)
def load_previous_district(request):
    previous_districts = list(District.objects.values_list('name', flat=True))
    return JsonResponse(previous_districts, safe=False)
def load_previous_upazilla(request):
    previous_upazillas = list(Upazilla.objects.values_list('name', flat=True))
    return JsonResponse(previous_upazillas, safe=False)
def load_previous_union(request):
    previous_unions = list(Union.objects.values_list('name', flat=True))
    return JsonResponse(previous_unions, safe=False)
def load_previous_user(request):
    previous_users = list(User.objects.values_list('first_name', flat=True))
    return JsonResponse(previous_users, safe=False)
