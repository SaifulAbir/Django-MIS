from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from districts.models import District
from upazillas.models import Upazilla
from .forms import UpazillaForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

def save_upazilla_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            upazilla_list = Upazilla.objects.all()
            data['html_upazilla_list'] = render_to_string('upazillas/partial_upazillas_list.html',
                                                          {'upazilla_list': upazilla_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def upazilla_create(request):
    data = dict()

    if request.method == 'POST':
        form = UpazillaForm(request.POST)
    else:
        form = UpazillaForm()
    return save_upazilla_form(request, form, 'upazillas/upazilla_form.html')

def upazilla_update(request, pk):
    upazilla = get_object_or_404(Upazilla, pk=pk)
    if request.method == 'POST':
        form = UpazillaForm(request.POST, instance=upazilla)
    else:
        form = UpazillaForm(instance=upazilla)
    return save_upazilla_form(request, form, 'upazillas/upazilla_update_form.html')


class UpazillaList(LoginRequiredMixin, generic.ListView):

    model = models.Upazilla


def upazilla_delete(request, pk):
    upazilla = get_object_or_404(Upazilla, pk=pk)
    data = dict()
    if request.method == 'POST':
        upazilla.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        upazilla_list = Upazilla.objects.all()
        data['html_upazilla_list'] = render_to_string('upazillas/partial_upazillas_list.html', {
            'upazilla_list': upazilla_list
        })
    else:
        context = {'upazilla': upazilla}
        data['html_form'] = render_to_string('upazillas/upazilla_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'upazillas/district_dropdown_list_options.html', {'districts': districts})
