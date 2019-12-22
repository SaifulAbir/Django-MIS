from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
            districts = District.objects.all()
            paginator = Paginator(districts, 10)
            page = request.GET.get('page')

            try:
                district_list = paginator.page(page)
            except PageNotAnInteger:
                district_list = paginator.page(1)
            except EmptyPage:
                district_list = paginator.page(paginator.num_pages)
            data['html_list'] = render_to_string('districts/partial_districts_list.html',
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
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super(DistrictList, self).get_context_data(**kwargs)
        districts = District.objects.all()
        paginator = Paginator(districts, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            district_list = paginator.page(page)
        except PageNotAnInteger:
            district_list = paginator.page(1)
        except EmptyPage:
            district_list = paginator.page(paginator.num_pages)

        context['district_list'] = district_list
        return context


def district_delete(request, pk):
    district = get_object_or_404(District, pk=pk)
    data = dict()
    if request.method == 'POST':
        district.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        districts = District.objects.all()
        paginator = Paginator(districts, 10)
        page = request.GET.get('page')
        try:
            district_list = paginator.page(page)
        except PageNotAnInteger:
            district_list = paginator.page(1)
        except EmptyPage:
            district_list = paginator.page(paginator.num_pages)
        data['html_list'] = render_to_string('districts/partial_districts_list.html', {
            'district_list': district_list
        })
    else:
        context = {'district': district}
        data['html_form'] = render_to_string('districts/district_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    districts = District.objects.all()
    paginator = Paginator(districts, 10)
    page = request.GET.get('page')
    try:
        district_list = paginator.page(page)
    except PageNotAnInteger:
        district_list = paginator.page(1)
    except EmptyPage:
        district_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('districts/partial_districts_list.html', {
        'district_list': district_list
    })
    return JsonResponse(data)

