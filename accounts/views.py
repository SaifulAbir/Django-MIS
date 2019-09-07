from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/')
def index(request):
    context = {'PROJECT_NAME': settings.PROJECT_NAME}
    return render(request, 'sknf/index.html', context)
