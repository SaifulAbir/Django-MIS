from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.base import ContentFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import base64
import uuid
# Create your views here.
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import generic

from accounts.decorators import headmaster_mentor_skleader_login_required, admin_login_required
from accounts.models import User
from eduplus_activity import models
from eduplus_activity.forms import EduPlusActivityForm, EditEduPlusActivityForm, MethodForm
from eduplus_activity.models import EduPlusActivity, Method
from eduplus_activity.resources import EduPlusActivityResource
from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from topics.models import Topics
from . import strings as edu_strings
from resources import strings as common_strings
from datetime import datetime


@headmaster_mentor_skleader_login_required
def edu_plus_activity_add(request):
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)

    if profile is not None:
        school_profile = get_object_or_404(School, pk=profile.school.id)
    else:
        school_profile = None
    if school_profile is not None:
        try:
            sk_profile = SkLeaderProfile.objects.filter(school__id=school_profile.id,
                                                                  user__user_type=5).latest('school__id')
        except SkLeaderProfile.DoesNotExist:
            sk_profile = None
    if request.method == 'POST':
        edu_plus_activity_form = EduPlusActivityForm(request.POST, files=request.FILES, prefix='EPA', user=request.user)
        # meeting_topic_form = MeetingmethodForm(request.POST, prefix='MTF')
        if edu_plus_activity_form.is_valid():
            edu_plus_activity = edu_plus_activity_form.save(commit=False)
            edu_plus_activity.school = profile.school
            if sk_profile:
                edu_plus_activity.skleader = sk_profile
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
            messages.success(request, edu_strings.EDUPLUS_ACTIVITY_CREATED_MSG)
            return HttpResponseRedirect("/eduplus_activity/eduplus_activity_list/")

    else:
        edu_plus_activity_form = EduPlusActivityForm(prefix='EPA', user=request.user)
        # meeting_topic_form = MeetingmethodForm(prefix='MTF')
        #headmaster_form_details = HeadmasterDetailsForm(prefix='hf')

    return render(request, 'eduplus_activity/eduplus_activity_add.html', {
        'edu_plus_activity_form': edu_plus_activity_form,'edu_strings':edu_strings,'common_strings':common_strings
        #'headmaster_form_details': headmaster_form_details,
    })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class EduplusActivityList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.EduPlusActivity
    paginate_by = 10
    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        queryset = EduPlusActivity.objects.filter(school=profile.school)
        return queryset
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        eduplus_activities = EduPlusActivity.objects.filter(school=profile.school)
        paginator = Paginator(eduplus_activities, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            eduplus_activity_list = paginator.page(page)
        except PageNotAnInteger:
            eduplus_activity_list = paginator.page(1)
        except EmptyPage:
            eduplus_activity_list = paginator.page(paginator.num_pages)
        context['eduplus_activity_list'] = eduplus_activity_list
        context['edu_strings'] = edu_strings
        context['common_strings'] = common_strings
        return context


@headmaster_mentor_skleader_login_required
def edu_plus_activity_update(request, pk):
    edu_plus_activity = get_object_or_404(EduPlusActivity, pk=pk)
    # prev_member = ClubMeetings.attendance.through.objects.filter(clubmeetings_id=club_meeting)
    all_member = SkMemberProfile.objects.filter(school__id=edu_plus_activity.school.id)
    # all_member = User.objects.filter(skmember_profile__in=sk_profile)
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
            messages.success(request, edu_strings.EDUPLUS_ACTIVITY_UPDATED_MSG)
            return HttpResponseRedirect("/eduplus_activity/eduplus_activity_list/")
    else:
        edu_plus_activity_form = EditEduPlusActivityForm(instance=edu_plus_activity, prefix='EPA', user=request.user)

    return render(request, 'eduplus_activity/eduplus_activity_add.html', {
        'edu_plus_activity_form': edu_plus_activity_form,
        'eduplus_activity': edu_plus_activity,
        'all_member': all_member,
        'edu_strings':edu_strings,'common_strings':common_strings
    })

class EduplusActivityDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "eduplus_activity_detail"
    model = models.EduPlusActivity
    template_name = 'eduplus_activity/eduplus_activity_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edu_strings"] = edu_strings
        context["common_strings"] = common_strings
        return context


def save_method_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            methods = Method.objects.all()
            paginator = Paginator(methods, 10)
            page = request.GET.get('page')
            try:
                method_list = paginator.page(page)
            except PageNotAnInteger:
                method_list = paginator.page(1)
            except EmptyPage:
                method_list = paginator.page(paginator.num_pages)
            data['html_list'] = render_to_string('eduplus_activity/partial_method_list.html',
                                                          {'method_list': method_list,
                                                           'edu_strings':edu_strings,'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form,'edu_strings':edu_strings,'common_strings':common_strings}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def method_create(request):
    data = dict()

    if request.method == 'POST':
        form = MethodForm(request.POST)
    else:
        form = MethodForm()
    return save_method_form(request, form, 'eduplus_activity/method_form.html')

def method_update(request, pk):
    method = get_object_or_404(Method, pk=pk)
    if request.method == 'POST':
        form = MethodForm(request.POST, instance=method)
    else:
        form = MethodForm(instance=method)
    return save_method_form(request, form, 'eduplus_activity/method_update_form.html')

@method_decorator(admin_login_required, name='dispatch')
class EduplusTopicsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Method
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        methods = Method.objects.all()
        paginator = Paginator(methods, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            method_list = paginator.page(page)
        except PageNotAnInteger:
            method_list = paginator.page(1)
        except EmptyPage:
            method_list = paginator.page(paginator.num_pages)

        context['method_list'] = method_list
        context["edu_strings"] = edu_strings
        context["common_strings"] = common_strings
        return context

def method_delete(request, pk):
    method = get_object_or_404(Method, pk=pk)
    data = dict()
    if request.method == 'POST':
        method.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        methods = Method.objects.all()
        paginator = Paginator(methods, 10)
        page = request.GET.get('page')
        try:
            method_list = paginator.page(page)
        except PageNotAnInteger:
            method_list = paginator.page(1)
        except EmptyPage:
            method_list = paginator.page(paginator.num_pages)
        data['html_list'] = render_to_string('eduplus_activity/partial_method_list.html', {
            'method_list': method_list ,'edu_strings':edu_strings,'common_strings':common_strings
        })
    else:
        context = {'method': method,'edu_strings':edu_strings,'common_strings':common_strings}
        data['html_form'] = render_to_string('eduplus_activity/method_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

@admin_login_required
def eduplus_activity_report_list(request):
    eduplus_activity_list = EduPlusActivity.objects.all()
    topic = Topics.objects.all()
    method = Method.objects.all()
    paginator = Paginator(eduplus_activity_list, 10)
    page = request.GET.get('page')
    try:
        eduplus_activity_report = paginator.page(page)
    except PageNotAnInteger:
        eduplus_activity_report = paginator.page(1)
    except EmptyPage:
        eduplus_activity_report = paginator.page(paginator.num_pages)
    return render(request, 'eduplus_activity/eduplus_activity_report_list.html', {'eduplusactivity_list': eduplus_activity_report,'topic':topic,'method':method,
                                                                                  'edu_strings':edu_strings,'common_strings':common_strings})

def eduplus_activity_search_list(request, export='null'):
    data = dict()
    qs = EduPlusActivity.objects.all()
    name = request.GET.get('name_contains')
    division = request.GET.get('division_contains')
    district = request.GET.get('district_contains')
    upazila = request.GET.get('upazila_contains')
    union = request.GET.get('union_contains')
    from_date = request.GET.get('fromdate_contains')
    if from_date :
        fromdate = datetime.strptime(from_date,'%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        fromdate = from_date

    to_date = request.GET.get('todate_contains')
    print(to_date)
    if to_date:
        todate = datetime.strptime(to_date,'%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        todate = to_date

    topics = request.GET.get('topics_contains')
    method = request.GET.get('method_contains')

    if name != '' and name is not None:
        qs = qs.filter(school__name__icontains=name)
    if division != '' and division is not None:
        qs = qs.filter(school__division__name__icontains=division)
    if district != '' and district is not None:
        qs = qs.filter(school__district__name__icontains=district)
    if upazila != '' and upazila is not None:
        qs = qs.filter(school__upazilla__name__icontains=upazila)
    if union != '' and union is not None:
        qs = qs.filter(school__union__name__icontains=union)
    if topics != '' and topics is not None:
        qs = qs.filter(topics__name__icontains=topics)
    if method != '' and method is not None:
        qs = qs.filter(method__name__icontains=method)
    if fromdate:
        qs = qs.filter(date__gte=fromdate)
    if todate and not fromdate:
        qs = qs.filter(date__lte=todate)
    if from_date and to_date :
        qs = qs.filter(date__gte=fromdate, date__lte=todate)


    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and division == '' and district == '' and upazila== '' and union == '' and from_date == '' and to_date =='' and topics == '' and method == '':
        queryset = None
    data['form_is_valid'] = True
    data['html_list'] = render_to_string('eduplus_activity/partial_eduplus_activity_report.html',
                                                  {'eduplusactivity_list': queryset,
                                                   'edu_strings':edu_strings,'common_strings':common_strings})
    if export != 'export':
        return JsonResponse(data)
    else:
        resource = EduPlusActivityResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="eduplus_activity_list.csv"'
        return response

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    eduplus_activities = EduPlusActivity.objects.all()
    paginator = Paginator(eduplus_activities, 10)
    page = request.GET.get('page')
    try:
        eduplus_activity_list = paginator.page(page)
    except PageNotAnInteger:
        eduplus_activity_list = paginator.page(1)
    except EmptyPage:
        eduplus_activity_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('eduplus_activity/partial_eduplus_activity_list.html', {
        'eduplus_activity_list': eduplus_activity_list, 'edu_strings':edu_strings, 'common_strings':common_strings
    })
    return JsonResponse(data)

def method_pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    methods = Method.objects.all()
    paginator = Paginator(methods, 10)
    page = request.GET.get('page')
    try:
        method_list = paginator.page(page)
    except PageNotAnInteger:
        method_list = paginator.page(1)
    except EmptyPage:
        method_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('eduplus_activity/partial_method_list.html', {
        'method_list': method_list, 'edu_strings':edu_strings, 'common_strings':common_strings
    })
    return JsonResponse(data)