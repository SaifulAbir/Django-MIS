from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from districts.models import District
from .forms import DistrictForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


def save_district_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            district_list = District.objects.all()
            data['html_district_list'] = render_to_string('districts/partial_districts_list.html',
                                                          {'district_list': district_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def district_create(request):
    data = dict()

    if request.method == 'POST':
        form = DistrictForm(request.POST)
    else:
        form = DistrictForm()
    return save_district_form(request, form, 'districts/district_form.html')

def district_update(request, pk):
    district = get_object_or_404(District, pk=pk)
    if request.method == 'POST':
        form = DistrictForm(request.POST, instance=district)
    else:
        form = DistrictForm(instance=district)
    return save_district_form(request, form, 'districts/district_update_form.html')

@method_decorator(admin_login_required, name='dispatch')
class DistrictList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.District

"""class DeleteDistrict(LoginRequiredMixin, generic.DeleteView):

    model = models.District
    success_url = reverse_lazy('districts:district_list')"""

def district_delete(request, pk):
    district = get_object_or_404(District, pk=pk)
    data = dict()
    if request.method == 'POST':
        district.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        district_list = District.objects.all()
        data['html_district_list'] = render_to_string('districts/partial_districts_list.html', {
            'district_list': district_list
        })
    else:
        context = {'district': district}
        data['html_form'] = render_to_string('districts/district_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)


