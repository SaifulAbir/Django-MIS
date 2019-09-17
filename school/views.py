from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from districts.models import District
from school.models import School
from unions.models import Union
from upazillas.models import Upazilla
from .forms import SchoolForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


class CreateSchool(LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    form_class = SchoolForm
    model = School

class SchoolUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    form_class = SchoolForm
    model = models.School


class SchoolDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "school_detail"
    model = models.School
    template_name = 'school/school_detail.html'

def save_school_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            school_list = School.objects.all()
            data['html_school_list'] = render_to_string('school/partial_school_list.html',
                                                          {'school_list': school_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

"""def school_create(request):
    data = dict()

    if request.method == 'POST':
        form = SchoolForm(request.POST)
    else:
        form = SchoolForm()
    return save_school_form(request, form, 'school/school_form.html')"""

def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
    else:
        form = SchoolForm(instance=school)
    return save_school_form(request, form, 'school/school_update_form.html')


class SchoolList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.School

"""class DeleteDistrict(LoginRequiredMixin, generic.DeleteView):

    model = models.District
    success_url = reverse_lazy('districts:district_list')"""

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    data = dict()
    if request.method == 'POST':
        school.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        school_list = School.objects.all()
        data['html_school_list'] = render_to_string('school/school_list.html', {
            'school_list': school_list
        })
    else:
        context = {'school': school}
        data['html_form'] = render_to_string('school/school_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'school/district_dropdown_list_options.html', {'districts': districts})

def load_upazillas(request):
    district_id = request.GET.get('district')
    upazillas = Upazilla.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'school/upazilla_dropdown_list_options.html', {'upazillas': upazillas})

def load_unions(request):
    upazilla_id = request.GET.get('upazilla')
    unions = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    return render(request, 'school/union_dropdown_list_options.html', {'unions': unions})

def school_profile(request, pk):
    name = School.objects.get(pk=pk)
    return render(request, 'school/school_profile.html', { 'name' : name})

def Sk_leaderApproval(request):
    return render(request, 'school/Sk_leaderApproval.html')
