from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_mentor_skleader_login_required
from club_meetings import models
from club_meetings.models import ClubMeetings
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from .forms import ClubMeetingForm, EditClubMeetingForm


# Create your views here.
@headmaster_mentor_skleader_login_required
def club_meeting_add(request):
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    if request.method == 'POST':
        club_meeting_form = ClubMeetingForm(request.POST, files=request.FILES, prefix='CMF', user=request.user)
        # meeting_topic_form = MeetingTopicsForm(request.POST, prefix='MTF')
        if club_meeting_form.is_valid():
            club_meeting = club_meeting_form.save(commit=False)
            club_meeting.school = profile.school
            club_meeting.save()
            club_meeting_form.save_m2m()
            messages.success(request, 'Club Meeting Created!')
            # meeting_topic = meeting_topic_form.save(commit = False)
            # meeting_topic.club_meeting = club_meeting
            # meeting_topic.save()
            # meeting_topic_form.save_m2m()
            return HttpResponseRedirect("/club_meetings/club_meeting_list/")

    else:
        club_meeting_form = ClubMeetingForm(prefix='CMF', user=request.user)
        # meeting_topic_form = MeetingTopicsForm(prefix='MTF')
        #headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'club_meetings/club_meeting_add.html', {
        'club_meeting_form': club_meeting_form,
        #'headmaster_form_details': headmaster_form_details,
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class ClubMeetingsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.ClubMeetings

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        queryset = ClubMeetings.objects.filter(school=profile.school)
        return queryset

@headmaster_mentor_skleader_login_required
def club_meeting_update(request, pk):
    club_meeting = get_object_or_404(ClubMeetings, pk=pk)
    if request.method == 'POST':
        club_meeting_form = EditClubMeetingForm(request.POST, request.FILES, instance=club_meeting, prefix='CMF', user=request.user)
        if club_meeting_form.is_valid():
            club_meeting = club_meeting_form.save(commit=False)
            club_meeting.save()
            club_meeting_form.save_m2m()
            messages.success(request, 'Club Meeting Updated!')
            return HttpResponseRedirect("/club_meetings/club_meeting_list/")
    else:
        club_meeting_form = EditClubMeetingForm(instance=club_meeting, prefix='CMF', user=request.user)

    return render(request, 'club_meetings/club_meeting_add.html', {
        'club_meeting_form': club_meeting_form,
        'club_meeting': club_meeting,
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class ClubMeetingDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "club_meeting_detail"
    model = models.ClubMeetings
    template_name = 'club_meetings/club_meeting_detail.html'



