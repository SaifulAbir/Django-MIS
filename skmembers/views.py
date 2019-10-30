import base64
import uuid

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from accounts.decorators import admin_login_required, headmaster_mentor_skleader_login_required
from accounts.models import User
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers import models
from skmembers.forms import SkMemberUserForm, SkMemberProfileForm, EditSkMemberUserForm, SkMemberProfileFormForSkleader, \
    EditSkMemberProfileForm
from skmembers.models import SkMemberProfile,SkmemberDetails
from datetime import datetime
from .resources import SkmemberResource
from django.core.exceptions import ObjectDoesNotExist


@admin_login_required
def skmember_profile_view(request):
    if request.method == 'POST':
        user_form = SkMemberUserForm(request.POST, prefix='UF')
        profile_form = SkMemberProfileForm(request.POST, files=request.FILES, prefix='PF')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.user_type = 6
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-skmember.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/' + filename
            # end of image cropping code
            profile.save()

            headmaster_details = SkmemberDetails()
            headmaster_details.school = profile_form.cleaned_data["school"]
            headmaster_details.skmember = profile
            headmaster_details.from_date = profile_form.cleaned_data["joining_date"]
            headmaster_details.save()
            messages.success(request, 'SK Member Created!')
            return HttpResponseRedirect("/skmembers/skmember_list/")

    else:
        user_form = SkMemberUserForm(prefix='UF')
        profile_form = SkMemberProfileForm(prefix='PF')

    return render(request, 'skmembers/skmember_profile_add.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@headmaster_mentor_skleader_login_required
def skmember_profile_view_skleader(request):
    if request.method == 'POST':
        user_form = SkMemberUserForm(request.POST, prefix='UF')
        profile_form = SkMemberProfileFormForSkleader(request.POST, files=request.FILES, prefix='PF')
        if user_form.is_valid() and profile_form.is_valid():
            id = request.user.id
            if request.user.is_authenticated and request.user.user_type == 5:
                objSkLeader = SkLeaderProfile.objects.get(user_id=id)
            elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
                objSkLeader = HeadmasterProfile.objects.get(user_id=id)
            school_id = objSkLeader.school_id

            user = user_form.save(commit=False)
            user.user_type = 6
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.school_id = school_id
            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-skmember.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/' + filename
            # end of image cropping code
            profile.save()

            headmaster_details = SkmemberDetails()
            headmaster_details.school_id = school_id
            headmaster_details.skmember = profile
            headmaster_details.from_date = profile_form.cleaned_data["joining_date"]
            headmaster_details.save()
            return HttpResponseRedirect("/skmembers/skmember_list_for_skleader/")
    else:
        user_form = SkMemberUserForm(prefix='UF')
        profile_form = SkMemberProfileFormForSkleader(prefix='PF')

    return render(request, 'skmembers/skmember_profile_add_for_skleader.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

@headmaster_mentor_skleader_login_required
def skmember_update_for_skleader(request, pk):
    skmember_profile = get_object_or_404(SkMemberProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(skmember_profile.user.id))
    skmember_details = SkmemberDetails.objects.filter(skmember=pk)
    school_list = School.objects.all()
    if request.method == 'POST':
        user_form = EditSkMemberUserForm(request.POST, instance=user_profile)
        profile_form = EditSkMemberProfileForm(request.POST, request.FILES, instance=skmember_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # messages.success(request, 'SK Member Updated!')
            return HttpResponseRedirect("/skmembers/skmember_list_for_skleader/")
    else:
        user_form = EditSkMemberUserForm(instance=user_profile)
        profile_form = EditSkMemberProfileForm(instance=skmember_profile)

    return render(request, 'skmembers/skmember_profile_update_for_skleader.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skmember_profile': skmember_profile,
        'pk': pk,
        'skmember_details': skmember_details,
        'school_list': school_list,
    })

@method_decorator(admin_login_required, name='dispatch')
class SkmemberList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile
    def get_queryset(self):
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,])
        return queryset
    def get_context_data(self, **kwargs):
        context = super(SkmemberList, self).get_context_data(**kwargs)
        try:
            context['school_name'] =SkmemberDetails.objects.latest('from_date')
        except SkmemberDetails.DoesNotExist:
            context['current_schoxol_name'] = None

        return context

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class SkmemberListforSkLeader(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.SkMemberProfile
    template_name = 'skmembers/skmemberprofile_list_for_skleader.html'


    def get_queryset(self):
        loggedinuser = self.request.user.id
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            objSkLeader = SkLeaderProfile.objects.get(user_id=loggedinuser)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            objSkLeader = HeadmasterProfile.objects.get(user_id=loggedinuser)
        queryset = SkMemberProfile.objects.filter(user__user_type__in=[6,],school_id=objSkLeader.school_id)

        return queryset

def skmember_list(request,export='null'):
    qs=SkMemberProfile.objects.filter(user__user_type__in=[6])
    name= request.GET.get('name_contains')
    school= request.GET.get('school_contains')

    if name !='' and name is not None:
        qs = qs.filter(user__first_name__icontains=name)
    if school != '' and school is not None:
        qs = qs.filter(school__name__icontains=school)
    if export != 'export':
        return render(request, 'skmembers/skmemberprofile_list.html',
                      {'queryset': qs, 'name': name, 'school': school, })
    else:
        resource = SkmemberResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="skmember_list.csv"'
        return response

@admin_login_required
def skmember_update(request, pk):
    skmember_profile = get_object_or_404(SkMemberProfile, pk=pk)
    user_profile = get_object_or_404(User, pk=int(skmember_profile.user.id))
    skmember_details = SkmemberDetails.objects.filter(skmember=pk)
    school_list = School.objects.all()
    if request.method == 'POST':
        user_form = EditSkMemberUserForm(request.POST, instance=user_profile)
        profile_form = EditSkMemberProfileForm(request.POST, request.FILES, instance=skmember_profile, prefix='PF')
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            # image cropping code start here
            img_base64 = profile_form.cleaned_data.get('image_base64')
            if img_base64:
                format, imgstr = img_base64.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-skmember.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                profile.image.save(filename, data, save=True)
                profile.image = 'images/' + filename
            # end of image cropping code
            profile.save()
            messages.success(request, 'SK Member Updated!')
            return HttpResponseRedirect("/skmembers/skmember_list/")
    else:
        user_form = EditSkMemberUserForm(instance=user_profile)
        profile_form = EditSkMemberProfileForm(instance=skmember_profile, prefix='PF')

    return render(request, 'skmembers/skmember_profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'skmember_profile': skmember_profile,
        'pk': pk,
        'skmember_details': skmember_details,
        'school_list': school_list,
    })


class SkMemberDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "skmember_detail"
    model = models.SkMemberProfile
    template_name = 'skmembers/skmember_detail.html'

@admin_login_required
def skmember_details_update(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    skmember_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")

    SkmemberDetails.objects.filter(skmember = skmember_id).delete()
    current_school_index = len(school_list)
    for school in school_list:
        skmemberModel = SkmemberDetails()
        skmemberModel.skmember_id = skmember_id
        skmemberModel.school_id = school
        schoolindex = school_list.index(school)
        fromdate = datetime.strptime(from_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')

        skmemberModel.from_date = fromdate
        if schoolindex == current_school_index-1:
            skmember_obj=SkMemberProfile.objects.get(pk=skmember_id)
            skmember_obj.school_id = school
            skmember_obj.save()

        if to_date[schoolindex]:
            todate = datetime.strptime(to_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')
            skmemberModel.to_date = todate
        skmemberModel.save()
    return HttpResponse('ok')


def skmember_details_update_for_skleader(request):

    school = request.GET.get('school')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    skmember_id = request.GET.get('headmaster_id')

    school_list = school.split(",")
    from_date = from_date.split(",")
    to_date = to_date.split(",")

    SkmemberDetails.objects.filter(skmember = skmember_id).delete()
    current_school_index = len(school_list)
    for school in school_list:
        skmemberModel = SkmemberDetails()
        skmemberModel.skmember_id = skmember_id
        skmemberModel.school_id = school
        schoolindex = school_list.index(school)
        fromdate = datetime.strptime(from_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')

        skmemberModel.from_date = fromdate
        if schoolindex == current_school_index-1:
            skmember_obj=SkMemberProfile.objects.get(pk=skmember_id)
            skmember_obj.school_id = school
            skmember_obj.save()

        if to_date[schoolindex]:
            todate = datetime.strptime(to_date[schoolindex], '%d-%m-%Y').strftime('%Y-%m-%d')
            skmemberModel.to_date = todate
        skmemberModel.save()
    return HttpResponse('ok')