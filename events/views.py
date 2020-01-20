from datetime import datetime
from . import strings as event_strings
from resources import strings as common_strings
from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.decorators import admin_login_required
from events.models import Event
from events.resources import EventResource


@admin_login_required
def create_event(request):
    event_list = Event.objects.all()
    context = {'event_list': event_list, 'event_strings': event_strings, 'common_strings':common_strings}
    return render(request, 'events/create_event.html', context)

@admin_login_required
def add_event(request):

    eventId = request.POST.get('eventId')
    title = request.POST.get('title')
    start = request.POST.get('start')
    end = request.POST.get('end')
    print(start)
    print(end)
    start_date = start
    end_date = end
    # start_date = datetime.strptime(start, '%d-%m-%Y %H:%M %p').strftime('%Y-%m-%d %H:%M:%S')
    # end_date = datetime.strptime(end, '%d-%m-%Y %H:%M %p').strftime('%Y-%m-%d %H:%M:%S')
    if eventId:
        evenObj = Event.objects.get(id=eventId)
        evenObj.title = title
        evenObj.start_date = start_date
        evenObj.end_date = end_date
        evenObj.save()
    else:
        if title and start:
            event = Event(title=title,start_date=start_date,end_date=end_date)
            event.save()
    return HttpResponse('ok')

@admin_login_required
def delete_event(request):
    eventId = request.POST.get('eventId')
    Event.objects.filter(id=eventId).delete()
    return HttpResponse('ok')

def event_list(request):
    qs = Event.objects.all()
    from_date = request.POST.get('start_date')
    print(from_date)
    if from_date :
        fromdate = datetime.strptime(from_date,'%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        fromdate = from_date

    to_date = request.POST.get('end_date')
    if to_date:
        todate = datetime.strptime(to_date,'%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        todate = to_date

    if fromdate:
        qs = qs.filter(start_date__gte=fromdate)
    if todate and not fromdate:
        qs = qs.filter(end_date__lte=todate)
    if from_date and to_date :
        qs = qs.filter(start_date__gte=fromdate, end_date__lte=todate)
    resource = EventResource()
    dataset = resource.export(qs)
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="event_list.csv"'
    return response

