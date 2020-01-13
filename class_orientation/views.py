from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
import class_orientation.strings as peer_education_strings
from resources import strings as common_strings
from accounts.decorators import headmaster_mentor_skleader_login_required, admin_login_required
from class_orientation.resources import PeerEducationResource
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from topics.models import Topics
from .models import PeerEducation
from .forms import PeerEducationForm
from datetime import datetime
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

def peer_education_form(request, form, template_name):
    data = dict()
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            peer_education_form = form.save(commit=False)
            peer_education_form.school = profile.school
            peer_education_form.save()
            form.save_m2m()
            data['form_is_valid'] = True
            if request.user.is_authenticated and request.user.user_type == 5:
                profile = SkLeaderProfile.objects.get(user=request.user)
            elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
                profile = HeadmasterProfile.objects.get(user=request.user)
            peer_educations = PeerEducation.objects.filter(school=profile.school)
            paginator = Paginator(peer_educations, 10)
            page = request.GET.get('page')
            try:
                peereducation_list = paginator.page(page)
            except PageNotAnInteger:
                peereducation_list = paginator.page(1)
            except EmptyPage:
                peereducation_list = paginator.page(paginator.num_pages)
            data['html_peer_education_list'] = render_to_string('peer_education/partial_peer_education_list.html',
                                                                {'peereducation_list': peereducation_list, 'common_strings':common_strings, 'peer_education_strings':peer_education_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'common_strings':common_strings, 'peer_education_strings':peer_education_strings}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def peer_education_add(request):
    data = dict()

    if request.method == 'POST':
        form = PeerEducationForm(request.POST)
    else:
        form = PeerEducationForm()
    return peer_education_form(request, form, 'peer_education/peer_education_form.html')

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class PeerEducationList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.PeerEducation
    template_name = 'peer_education/peereducation_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PeerEducationList, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        peer_educations = PeerEducation.objects.filter(school=profile.school)
        paginator = Paginator(peer_educations, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            peereducation_list = paginator.page(page)
        except PageNotAnInteger:
            peereducation_list = paginator.page(1)
        except EmptyPage:
            peereducation_list = paginator.page(paginator.num_pages)

        context['peereducation_list'] = peereducation_list
        context['common_strings'] = common_strings
        context['peer_education_strings'] = peer_education_strings
        return context

@headmaster_mentor_skleader_login_required
def peer_education_update(request, pk):
    peer_education = get_object_or_404(PeerEducation, pk=pk)
    if request.method == 'POST':
        form = PeerEducationForm(request.POST, instance=peer_education)
    else:
        form = PeerEducationForm(instance=peer_education)

    return peer_education_form(request, form, 'peer_education/peer_education_update_form.html')

@admin_login_required
def peer_education_report_list(request):
    topics = Topics.objects.all()
    peer_education_list = PeerEducation.objects.all()
    paginator = Paginator(peer_education_list, 10)
    page = request.GET.get('page')
    try:
        peer_education_report = paginator.page(page)
    except PageNotAnInteger:
        peer_education_report = paginator.page(1)
    except EmptyPage:
        peer_education_report = paginator.page(paginator.num_pages)
    return render(request, 'peer_education/peer_education_report_list.html', {'peereducation_list': peer_education_report, 'num_pages': paginator.count,
                                                                              'peer_education_strings': peer_education_strings,
                                                                              'common_strings': common_strings, 'topics':topics
                                                                              })

def peer_education_search_list(request, export='null'):
    data = dict()
    qs = PeerEducation.objects.all()
    name = request.POST.get('school_contains')
    division = request.POST.get('division_contains')
    district = request.POST.get('district_contains')
    upazila = request.POST.get('upazila_contains')
    union = request.POST.get('union_contains')
    from_date = request.POST.get('fromdate_contains')
    if from_date:
        fromdate = datetime.strptime(from_date, '%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        fromdate = from_date
    to_date = request.POST.get('todate_contains')
    if to_date:
        todate = datetime.strptime(to_date, '%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        todate = to_date
    topics = request.POST.get('topics_contains')
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
    if topics!= '' and topics is not None:
        qs = qs.filter(topic__name__icontains=topics)
    if fromdate:
        qs = qs.filter(created_date__gte=fromdate)
    if todate and not fromdate:
        qs = qs.filter(created_date__lte=todate)
    if from_date and to_date:
        qs = qs.filter(created_date__gte=fromdate, created_date__lte=todate)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and division == '' and district == '' and upazila== '' and union == '' and from_date == '' and to_date =='' and topics == '':
        queryset = None
    data['form_is_valid'] = True
    data['html_list'] = render_to_string('peer_education/partial_peer_education_report.html',
                                         {'peereducation_list': queryset, 'peer_education_strings': peer_education_strings,
                                          'common_strings': common_strings})
    if export != 'export':
        return JsonResponse(data)
    else:
        resource = PeerEducationResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="peer_education_list.csv"'
        return response

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    peer_educations = PeerEducation.objects.filter(school=profile.school)
    paginator = Paginator(peer_educations, 10)
    page = request.GET.get('page')
    try:
        peereducation_list = paginator.page(page)
    except PageNotAnInteger:
        peereducation_list = paginator.page(1)
    except EmptyPage:
        peereducation_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('peer_education/partial_peer_education_list.html', {
        'peereducation_list': peereducation_list, 'common_strings':common_strings,'peer_education_strings':peer_education_strings
    })
    return JsonResponse(data)