from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator

from accounts.decorators import headmaster_mentor_skleader_login_required, admin_login_required
from class_orientation.resources import ClassOrientationResource
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from .models import ClassOrientation
from .forms import ClassOrientationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

def class_orientation_form(request, form, template_name):
    data = dict()
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            class_orientation_form = form.save(commit=False)
            class_orientation_form.school = profile.school
            class_orientation_form.save()
            form.save_m2m()
            data['form_is_valid'] = True
            if request.user.is_authenticated and request.user.user_type == 5:
                profile = SkLeaderProfile.objects.get(user=request.user)
            elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
                profile = HeadmasterProfile.objects.get(user=request.user)
            classorientation_list = ClassOrientation.objects.filter(school=profile.school)
            data['html_class_orientation_list'] = render_to_string('class_orientation/partial_class_orientation_list.html',
                                                            {'classorientation_list': classorientation_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def class_orientation_add(request):
    data = dict()

    if request.method == 'POST':
        form = ClassOrientationForm(request.POST)
    else:
        form = ClassOrientationForm()
    return class_orientation_form(request, form, 'class_orientation/class_orientation_form.html')

# @headmaster_mentor_skleader_login_required
# def class_orientation_add(request):
#     if request.user.is_authenticated and request.user.user_type == 5:
#         profile = SkLeaderProfile.objects.get(user=request.user)
#     elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
#         profile = HeadmasterProfile.objects.get(user=request.user)
#     if request.method == 'POST':
#         class_orientation_form = ClassOrientationForm(request.POST, prefix='COF')
#         if class_orientation_form.is_valid():
#             class_orientation = class_orientation_form.save(commit=False)
#             class_orientation.school = profile.school
#             class_orientation.save()
#             messages.success(request, 'Class Orientation Created!')
#             return HttpResponseRedirect("/class_orientation/class_orientation_list/")
#
#     else:
#         class_orientation_form = ClassOrientationForm(prefix='COF')
#
#     return render(request, 'class_orientation/classorientation_form.html', {
#         'class_orientation_form': class_orientation_form,
#     })

@method_decorator(headmaster_mentor_skleader_login_required, name='dispatch')
class ClubOrientationsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.ClassOrientation

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=self.request.user)
        elif self.request.user.is_authenticated and self.request.user.user_type == 2 or self.request.user.user_type == 3 or self.request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=self.request.user)
        queryset = ClassOrientation.objects.filter(school=profile.school)
        return queryset

# @headmaster_mentor_skleader_login_required
# def class_orientation_update(request, pk):
#     class_orientation = get_object_or_404(ClassOrientation, pk=pk)
#     if request.method == 'POST':
#         class_orientation_form = ClassOrientationForm(request.POST, instance=class_orientation, prefix='COF')
#         if class_orientation_form.is_valid():
#             class_orientation = class_orientation_form.save(commit=False)
#             class_orientation.save()
#             messages.success(request, 'Class Orientation Updated!')
#             return HttpResponseRedirect("/class_orientation/class_orientation_list/")
#
#     else:
#         class_orientation_form = ClassOrientationForm(instance=class_orientation, prefix='COF')
#
#     return render(request, 'class_orientation/classorientation_form.html', {
#         'class_orientation_form': class_orientation_form,
#     })

@headmaster_mentor_skleader_login_required
def class_orientation_update(request, pk):
    class_orientation = get_object_or_404(ClassOrientation, pk=pk)
    if request.method == 'POST':
        form = ClassOrientationForm(request.POST, instance=class_orientation)
    else:
        form = ClassOrientationForm(instance=class_orientation)

    return class_orientation_form(request, form, 'class_orientation/classorientation_update_form.html')

@admin_login_required
def class_orientation_report_list(request):
    class_orientation_list = ClassOrientation.objects.all()
    paginator = Paginator(class_orientation_list, 10)
    page = request.GET.get('page')
    try:
        class_orientation_report = paginator.page(page)
    except PageNotAnInteger:
        class_orientation_report = paginator.page(1)
    except EmptyPage:
        class_orientation_report = paginator.page(paginator.num_pages)
    return render(request, 'class_orientation/class_orientation_report_list.html', {'classorientation_list': class_orientation_report, 'num_pages': paginator.count,})

def class_orientation_search_list(request, export='null'):
    data = dict()
    qs = ClassOrientation.objects.all()
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
    data['html_list'] = render_to_string('class_orientation/partial_class_orientation_report.html',
                                                  {'classorientation_list': queryset})
    if export != 'export':
        return JsonResponse(data)
    else:
        resource = ClassOrientationResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="peer_education_list.csv"'
        return response
