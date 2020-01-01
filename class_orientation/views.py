from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator

from accounts.decorators import headmaster_mentor_skleader_login_required, admin_login_required
from class_orientation.resources import PeerEducationResource
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from .models import PeerEducation
from .forms import PeerEducationForm
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
            peer_education_list = PeerEducation.objects.filter(school=profile.school)
            data['html_peer_education_list'] = render_to_string('peer_education/partial_peer_education_list.html',
                                                            {'peereducation_list': peer_education_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def peer_education_add(request):
    data = dict()

    if request.method == 'POST':
        form = PeerEducationForm(request.POST)
    else:
        form = PeerEducationForm()
    return peer_education_form(request, form, 'peer_education/peer_education_form.html')

# @headmaster_mentor_skleader_login_required
# def peer_education_add(request):
#     if request.user.is_authenticated and request.user.user_type == 5:
#         profile = SkLeaderProfile.objects.get(user=request.user)
#     elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
#         profile = HeadmasterProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         peer_education_form = PeerEducationForm(request.POST, prefix='COF')
#         if peer_education_form.is_valid():
#             peer_education = peer_education_form.save(commit=False)
#             peer_education.school = profile.school
#             peer_education.save()
#             messages.success(request, 'Class Orientation Created!')
#             return HttpResponseRedirect("/peer_education/peer_education_list/")
#
#     else:
#         peer_education_form = PeerEducationForm(prefix='COF')
#
#     return render(request, 'peer_education/peer_education_form.html', {
#         'peer_education_form': peer_education_form,
#     })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class PeerEducationList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.PeerEducation
    template_name = 'peer_education/peereducation_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        queryset = PeerEducation.objects.filter(school=profile.school)
        return queryset

# @headmaster_mentor_skleader_login_required
# def peer_education_update(request, pk):
#     peer_education = get_object_or_404(PeerEducation, pk=pk)
#     if request.method == 'POST':
#         peer_education_form = PeerEducationForm(request.POST, instance=peer_education, prefix='COF')
#         if peer_education_form.is_valid():
#             peer_education = peer_education_form.save(commit=False)
#             peer_education.save()
#             messages.success(request, 'Class Orientation Updated!')
#             return HttpResponseRedirect("/peer_education/peer_education_list/")
#
#     else:
#         peer_education_form = PeerEducationForm(instance=peer_education, prefix='COF')
#
#     return render(request, 'peer_education/peer_education_form.html', {
#         'peer_education_form': peer_education_form,
#     })

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
    peer_education_list = PeerEducation.objects.all()
    paginator = Paginator(peer_education_list, 10)
    page = request.GET.get('page')
    try:
        peer_education_report = paginator.page(page)
    except PageNotAnInteger:
        peer_education_report = paginator.page(1)
    except EmptyPage:
        peer_education_report = paginator.page(paginator.num_pages)
    return render(request, 'peer_education/peer_education_report_list.html', {'peereducation_list': peer_education_report, 'num_pages': paginator.count,})

def peer_education_search_list(request, export='null'):
    data = dict()
    qs = PeerEducation.objects.all()
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
    data['html_list'] = render_to_string('peer_education/partial_peer_education_report.html',
                                                  {'peereducation_list': queryset})
    if export != 'export':
        return JsonResponse(data)
    else:
        resource = PeerEducationResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="peer_education_list.csv"'
        return response
