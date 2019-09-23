from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect



# Create your views here.
from accounts.forms import PrettyAuthenticationForm
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
    return render(request, 'accounts/profile.html')


@login_required(login_url='/')
def events(request):
    return render(request, 'sknf/events.html')




def custom_login(request,):
    next_destination = request.GET.get('next')
    if request.user.is_authenticated and request.user.user_type == 1:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/dashboard/')
    elif request.user.is_authenticated and request.user.user_type == 2:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/school/school_profile')
    elif request.user.is_authenticated and request.user.user_type == 3:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/headmaster_home/')
    elif request.user.is_authenticated and request.user.user_type == 5:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/headmaster_home/')
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
                    headmaster_profile = HeadmasterProfile.objects.get(user=user)
                    return redirect('/headmasters/headmaster_home/')
                elif user.user_type == 5:
                    return redirect('/headmasters/headmaster_home/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = PrettyAuthenticationForm()

    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form, 'next_destination': next_destination})


