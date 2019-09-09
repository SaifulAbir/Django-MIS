from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
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




