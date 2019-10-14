from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from districts.models import District
from unions.models import Union
from upazillas.models import Upazilla

from .forms import UnionForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


def save_union_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            union_list = Union.objects.all()
            data['html_union_list'] = render_to_string('unions/partial_union_list.html',
                                                          {'union_list': union_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def union_create(request):
    data = dict()

    if request.method == 'POST':
        form = UnionForm(request.POST)
    else:
        form = UnionForm()
    return save_union_form(request, form, 'unions/union_form.html')

def union_update(request, pk):
    union = get_object_or_404(Union, pk=pk)
    if request.method == 'POST':
        form = UnionForm(request.POST, instance=union)
    else:
        form = UnionForm(instance=union)
    return save_union_form(request, form, 'unions/union_update_form.html')


@method_decorator(admin_login_required, name='dispatch')
class UnionList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Union

"""class DeleteDistrict(LoginRequiredMixin, generic.DeleteView):

    model = models.District
    success_url = reverse_lazy('districts:district_list')"""

def union_delete(request, pk):
    union = get_object_or_404(Union, pk=pk)
    data = dict()
    if request.method == 'POST':
        union.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        union_list = Union.objects.all()
        data['html_union_list'] = render_to_string('unions/partial_union_list.html', {
            'union_list': union_list
        })
    else:
        context = {'union': union}
        data['html_form'] = render_to_string('unions/union_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'unions/district_dropdown_list_options.html', {'districts': districts})

def load_upazillas(request):
    district_id = request.GET.get('district')
    upazillas = Upazilla.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'unions/upazilla_dropdown_list_options.html', {'upazillas': upazillas})

def load_unions(request):
    upazilla_id = request.GET.get('upazilla')
    unions = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    return render(request, 'unions/union_dropdown_list_options.html', {'unions': unions})

