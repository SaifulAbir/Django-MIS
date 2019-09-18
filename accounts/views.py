from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect



# Create your views here.
from accounts.forms import PrettyAuthenticationForm
from school.models import School


@login_required(login_url='/')
def index(request):
    school_list = School.objects.all()
    school_total = School.objects.count()
    context = {'PROJECT_NAME': settings.PROJECT_NAME, 'school_list': school_list, 'school_total': school_total}
    return render(request, 'sknf/index.html', context)


@login_required(login_url='/')
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required(login_url='/')
def events(request):
    return render(request, 'sknf/events.html')


def headmaster_home(request):
    return render(request, 'accounts/headmaster_home.html')

def custom_login(request,):
    next_destination = request.GET.get('next')
    if request.user.is_authenticated and request.user.user_type == 1:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/dashboard/')
    elif request.user.is_authenticated and request.user.user_type == 2:
        if next_destination:
            return HttpResponse("Access denied")
        return HttpResponseRedirect('/headmaster_home/')
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
                    return redirect('/headmaster_home/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = PrettyAuthenticationForm()

    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form, 'next_destination': next_destination})


