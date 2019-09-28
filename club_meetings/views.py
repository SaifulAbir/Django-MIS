from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from club_meetings import models
from club_meetings.models import ClubMeetings
from .forms import ClubMeetingForm


# Create your views here.
def club_meeting_add(request):

    if request.method == 'POST':
        club_meeting_form = ClubMeetingForm(request.POST, files=request.FILES, prefix='CMF')
        # meeting_topic_form = MeetingTopicsForm(request.POST, prefix='MTF')
        if club_meeting_form.is_valid():
            club_meeting = club_meeting_form.save(commit=False)
            club_meeting.save()
            club_meeting_form.save_m2m()
            # meeting_topic = meeting_topic_form.save(commit = False)
            # meeting_topic.club_meeting = club_meeting
            # meeting_topic.save()
            # meeting_topic_form.save_m2m()
            return HttpResponseRedirect("/club_meetings/club_meeting_list/")

    else:
        club_meeting_form = ClubMeetingForm(prefix='CMF')
        # meeting_topic_form = MeetingTopicsForm(prefix='MTF')
        #headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'club_meetings/club_meeting_add.html', {
        'club_meeting_form': club_meeting_form,
        #'headmaster_form_details': headmaster_form_details,
    })

class ClubMeetingsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.ClubMeetings

def club_meeting_update(request, pk):

    club_meeting = get_object_or_404(ClubMeetings, pk=pk)
    if request.method == 'POST':
        club_meeting_form = ClubMeetingForm(request.POST, request.FILES, instance=club_meeting, prefix='CMF')
        if club_meeting_form.is_valid():
            club_meeting = club_meeting_form.save(commit=False)
            club_meeting.save()
            club_meeting_form.save_m2m()
            return HttpResponseRedirect("/club_meetings/club_meeting_list/")
    else:
        club_meeting_form = ClubMeetingForm(instance=club_meeting, prefix='CMF')

    return render(request, 'club_meetings/club_meeting_add.html', {
        'club_meeting_form': club_meeting_form,
        'club_meeting': club_meeting,
    })

