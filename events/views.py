from datetime import datetime

from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from events.models import Event


def create_event(request):
    event_list = Event.objects.all()
    context = {'event_list': event_list}
    return render(request, 'events/create_event.html', context)

def add_event(request):
    title = request.POST.get('title')
    start = request.POST.get('start')
    end = request.POST.get('end')
    start_date = datetime.strptime(start, '%d-%m-%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(end, '%d-%m-%Y').strftime('%Y-%m-%d')
    print(title)
    if title and start:
        event = Event(title=title,start_date=start_date,end_date=end_date)
        event.save()
    return HttpResponse('ok')
