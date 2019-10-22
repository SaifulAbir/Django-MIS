from datetime import datetime

from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.decorators import admin_login_required
from events.models import Event

@admin_login_required
def create_event(request):
    event_list = Event.objects.all()
    context = {'event_list': event_list}
    return render(request, 'events/create_event.html', context)

@admin_login_required
def add_event(request):
    title = request.POST.get('title')
    start = request.POST.get('start')
    end = request.POST.get('end')
    start_date = datetime.strptime(start, '%d-%m-%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(end, '%d-%m-%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S')
    print(title)
    if title and start:
        event = Event(title=title,start_date=start_date,end_date=end_date)
        event.save()
    return HttpResponse('ok')
