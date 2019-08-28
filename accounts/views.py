from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/')
def index(request):
    return render(request, 'sknf/index.html')
