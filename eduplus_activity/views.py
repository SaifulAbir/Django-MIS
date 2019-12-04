from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render
import base64
import uuid
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_mentor_skleader_login_required
from eduplus_activity import models
from eduplus_activity.forms import EduPlusActivityForm
from eduplus_activity.models import EduPlusActivity
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile


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
                filename = str(uuid.uuid4()) + '-club_meeting.' + ext
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