from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import base64
import uuid
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_mentor_skleader_login_required
from accounts.models import User
from eduplus_activity import models
from eduplus_activity.forms import EduPlusActivityForm, EditEduPlusActivityForm
from eduplus_activity.models import EduPlusActivity
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile


@headmaster_mentor_skleader_login_required
def edu_plus_activity_add(request):
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    if request.method == 'POST':
        edu_plus_activity_form = EduPlusActivityForm(request.POST, files=request.FILES, prefix='EPA', user=request.user)
        # meeting_topic_form = MeetingTopicsForm(request.POST, prefix='MTF')
        if edu_plus_activity_form.is_valid():
            edu_plus_activity = edu_plus_activity_form.save(commit=False)
            edu_plus_activity.school = profile.school
            # image cropping code start here
            img_base64 = edu_plus_activity_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-eduplus_activity.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                edu_plus_activity.image.save(filename, data, save=True)
                edu_plus_activity.image = 'images/' + filename
            # end of image cropping code
            edu_plus_activity.save()
            edu_plus_activity_form.save_m2m()
            messages.success(request, 'Eduplus Activity Created!')
            return HttpResponseRedirect("/eduplus_activity/eduplus_activity_list/")

    else:
        edu_plus_activity_form = EduPlusActivityForm(prefix='EPA', user=request.user)
        # meeting_topic_form = MeetingTopicsForm(prefix='MTF')
        #headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'eduplus_activity/eduplus_activity_add.html', {
        'edu_plus_activity_form': edu_plus_activity_form,
        #'headmaster_form_details': headmaster_form_details,
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class EduplusActivityList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.EduPlusActivity

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        queryset = EduPlusActivity.objects.filter(school=profile.school)
        return queryset

@headmaster_mentor_skleader_login_required
def edu_plus_activity_update(request, pk):
    edu_plus_activity = get_object_or_404(EduPlusActivity, pk=pk)
    # prev_member = ClubMeetings.attendance.through.objects.filter(clubmeetings_id=club_meeting)
    sk_profile = SkMemberProfile.objects.filter(school__id=edu_plus_activity.school.id, user__user_type=6)
    all_member = User.objects.filter(skmember_profile__in=sk_profile)
    if request.method == 'POST':
        edu_plus_activity_form = EditEduPlusActivityForm(request.POST, request.FILES, instance=edu_plus_activity, prefix='EPA', user=request.user )
        if edu_plus_activity_form.is_valid():
            edu_plus_activity = edu_plus_activity_form.save(commit=False)
            # image cropping code start here
            img_base64 = edu_plus_activity_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-eduplus_activity.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                edu_plus_activity.image.save(filename, data, save=True)
                edu_plus_activity.image = 'images/' + filename
            # end of image cropping code
            edu_plus_activity.save()
            edu_plus_activity_form.save_m2m()
            messages.success(request, 'Eduplus Activity Updated!')
            return HttpResponseRedirect("/eduplus_activity/eduplus_activity_list/")
    else:
        edu_plus_activity_form = EditEduPlusActivityForm(instance=edu_plus_activity, prefix='EPA', user=request.user)

    return render(request, 'eduplus_activity/eduplus_activity_add.html', {
        'edu_plus_activity_form': edu_plus_activity_form,
        'eduplus_activity': edu_plus_activity,
        'all_member': all_member,
        'sk_lead': sk_profile
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class EduplusActivityDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "eduplus_activity_detail"
    model = models.EduPlusActivity
    template_name = 'eduplus_activity/eduplus_activity_detail.html'