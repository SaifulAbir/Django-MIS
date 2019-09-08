from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from division.models import Division
from .forms import DivisionForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


def save_division_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            division_list = Division.objects.all()
            data['html_division_list'] = render_to_string('division/partial_division_list.html',
                                                          {'division_list': division_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def division_create(request):
    data = dict()

    if request.method == 'POST':
        form = DivisionForm(request.POST)
    else:
        form = DivisionForm()
    return save_division_form(request, form, 'division/division_form.html')

def division_update(request, pk):
    division = get_object_or_404(Division, pk=pk)
    if request.method == 'POST':
        form = DivisionForm(request.POST, instance=division)
    else:
        form = DivisionForm(instance=division)
    return save_division_form(request, form, 'division/division_update_form.html')


class DivisionList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Division

"""class DeleteDistrict(LoginRequiredMixin, generic.DeleteView):

    model = models.District
    success_url = reverse_lazy('districts:district_list')"""

def division_delete(request, pk):
    division = get_object_or_404(Division, pk=pk)
    data = dict()
    if request.method == 'POST':
        division.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        division_list = Division.objects.all()
        data['html_division_list'] = render_to_string('division/partial_division_list.html', {
            'division_list': division_list
        })
    else:
        context = {'division': division}
        data['html_form'] = render_to_string('division/division_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
