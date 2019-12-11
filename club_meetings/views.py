import base64
import uuid

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_mentor_skleader_login_required, admin_login_required
from accounts.models import User
from club_meetings import models
from club_meetings.models import ClubMeetings
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
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
            # image cropping code start here
            img_base64 = club_meeting_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-club_meeting.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                club_meeting.image.save(filename, data, save=True)
                club_meeting.image = 'images/' + filename
            # end of image cropping code
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
    # prev_member = ClubMeetings.attendance.through.objects.filter(clubmeetings_id=club_meeting)
    sk_profile = SkMemberProfile.objects.filter(school__id=club_meeting.school.id, user__user_type=6)
    all_member = User.objects.filter(skmember_profile__in=sk_profile)
    if request.method == 'POST':
        club_meeting_form = EditClubMeetingForm(request.POST, request.FILES, instance=club_meeting, prefix='CMF', user=request.user )
        if club_meeting_form.is_valid():
            club_meeting = club_meeting_form.save(commit=False)
            # image cropping code start here
            img_base64 = club_meeting_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-club_meeting.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                club_meeting.image.save(filename, data, save=True)
                club_meeting.image = 'images/' + filename
            # end of image cropping code
            club_meeting.save()
            club_meeting_form.save_m2m()
            messages.success(request, 'Club Meeting Updated!')
            return HttpResponseRedirect("/club_meetings/club_meeting_list/")
    else:
        club_meeting_form = EditClubMeetingForm(instance=club_meeting, prefix='CMF', user=request.user)

    return render(request, 'club_meetings/club_meeting_add.html', {
        'club_meeting_form': club_meeting_form,
        'club_meeting': club_meeting,
        'all_member': all_member
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class ClubMeetingDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "club_meeting_detail"
    model = models.ClubMeetings
    template_name = 'club_meetings/club_meeting_detail.html'

@admin_login_required
def clubmeetings_report_list(request):
    clubmeetings_report = ClubMeetings.objects.all()
    paginator = Paginator(clubmeetings_report, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    return render(request, 'club_meetings/club_meeting_report_list.html', {'clubmeetings_list': queryset})

def club_meeting_search_list(request):
    data = dict()
    qs = ClubMeetings.objects.all()
    name = request.GET.get('name_contains')
    division = request.GET.get('division_contains')
    district = request.GET.get('district_contains')
    if name != '' and name is not None:
        qs = qs.filter(school__name__icontains=name)
    if division != '' and division is not None:
        qs = qs.filter(school__division__name__icontains=division)
    if district != '' and district is not None:
        qs = qs.filter(school__district__name__icontains=district)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and division == '' and district == '':
        queryset = None
    data['form_is_valid'] = True
    data['html_list'] = render_to_string('club_meetings/partial_club_meeting_report_list.html',
                                                  {'clubmeetings_list': queryset})
    return JsonResponse(data)



