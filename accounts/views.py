from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect



# Create your views here.
from accounts.forms import PrettyAuthenticationForm, EditUserForm, HeadmasterProfileForm, SkleaderProfileForm
from accounts.models import User
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile


@login_required(login_url='/')
def index(request):
    school_list = School.objects.all()
    school_total = School.objects.count()
    headmaster_total = User.objects.filter(user_type__in=[2,]).count()
    skleader_total = User.objects.filter(user_type__in=[5,]).count()
    skmember_total = User.objects.filter(user_type__in=[6,]).count()
    context = {'PROJECT_NAME': settings.PROJECT_NAME, 'school_list': school_list,
               'school_total': school_total, 'headmaster_total': headmaster_total, 'skleader_total': skleader_total, 'skmember_total': skmember_total}
    return render(request, 'sknf/index.html', context)


@login_required(login_url='/')
def profile(request):
    try:
        if request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
            h_profile = HeadmasterProfile.objects.get(user=request.user)
        elif request.user.is_authenticated and request.user.user_type == 5:
            h_profile = SkLeaderProfile.objects.get(user=request.user)
    except HeadmasterProfile.DoesNotExist:
        h_profile=None
    if h_profile is not None:
        school_profile = get_object_or_404(School, pk=h_profile.school.id)
    else:
        school_profile=None
    if school_profile is not None:
        headmaster_profile = HeadmasterProfile.objects.filter(school__id=school_profile.id, user__user_type=2).latest('school__id')
    else:
        headmaster_profile=None
    if school_profile is not None:
        skleader_profile = SkLeaderProfile.objects.filter(school__id=school_profile.id, user__user_type=5).latest('school__id')
    else:
        skleader_profile=None
    if request.user.is_authenticated and request.user.user_type == 1:
        profile = request.user
    elif request.user.is_authenticated and request.user.user_type == 2:
        profile = HeadmasterProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 3:
        profile = HeadmasterProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    else:
        profile = None

    return render(request, 'accounts/profile.html', {'profile': profile, 'headmaster_profile':headmaster_profile, 'skleader_profile':skleader_profile})


@login_required(login_url='/')
def events(request):
    return render(request, 'sknf/events.html')




def custom_login(request,):
    next_destination = request.GET.get('next')
    if request.user.is_authenticated and request.user.user_type == 1:
        if next_destination:
            return HttpResponse("Access denied")
        return redirect('/dashboard/')
    elif request.user.is_authenticated and request.user.user_type == 2:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            return HttpResponse("Access denied")
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 3:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            return HttpResponse("Access denied")
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 4:
        headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
        if next_destination:
            return HttpResponse("Access denied")
        return redirect('school:school_profile', headmaster_profile.school.id)
    elif request.user.is_authenticated and request.user.user_type == 5:
        skleader_profile = SkLeaderProfile.objects.get(user=request.user)
        if next_destination:
            return HttpResponse("Access denied")
        return redirect('school:school_profile', skleader_profile.school.id)
    else:
        return login_request(request)

def login_request(request):

    next_destination = request.GET.get('next')
    if request.method == 'POST':
        form = PrettyAuthenticationForm( data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
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
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = PrettyAuthenticationForm()

    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form, 'next_destination': next_destination})


def admin_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    old_password = user_profile.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, files=request.FILES, instance=user_profile)

        if user_form.is_valid():
            user_update = user_form.save(commit=False)
            user_update.user_type = 1
            form_password = user_form.cleaned_data["password"]
            if form_password:
                user_update.set_password(user_form.cleaned_data["password"])
            else:
                user_update.password = old_password
            user_update.save()
            update_session_auth_hash(request, user_update)
            return redirect("accounts:profile")

    else:
        user_form = EditUserForm(instance=user_profile)

    return render(request, 'accounts/admin_profile_form.html', {
        'user_form': user_form,
        'user_profile': user_profile
    })

def headmaster_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    headmaster_profile = HeadmasterProfile.objects.get(user=request.user)
    old_password = headmaster_profile.user.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile)
        profile_form = HeadmasterProfileForm(request.POST, request.FILES, instance=headmaster_profile)
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
            profile.save()
            return redirect("accounts:profile")
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = HeadmasterProfileForm(instance=headmaster_profile)

    return render(request, 'accounts/headmaster_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'headmaster_profile': headmaster_profile,
    })

def skleader_profile_update(request):
    user_profile = get_object_or_404(User, pk=request.user.id)
    skleader_profile = SkLeaderProfile.objects.get(user=request.user)
    old_password = skleader_profile.user.password
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user_profile)
        profile_form = SkleaderProfileForm(request.POST, request.FILES, instance=skleader_profile)
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
            profile.save()
            return redirect("accounts:profile")
    else:
        user_form = EditUserForm(instance=user_profile)
        profile_form = SkleaderProfileForm(instance=skleader_profile)

    return render(request, 'accounts/skleader_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skleader_profile': skleader_profile,
    })

