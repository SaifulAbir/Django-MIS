from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from Class_Orientation.models import Class_Orientation
from .forms import Class_OrientationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


def save_Class_Orientation_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            Class_Orientation_list = Class_Orientation.objects.all()
            data['html_Class_Orientation_list'] = render_to_string('Class_Orientation/partial_Class_Orientation_list.html',
                                                          {'Class_Orientation_list': Class_Orientation_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def Class_Orientation_create(request):
    data = dict()

    if request.method == 'POST':
        form = Class_OrientationForm(request.POST)
    else:
        form = Class_OrientationForm()
    return save_Class_Orientation_form(request, form, 'Class_Orientation/Class_Orientation_form.html')

def Class_Orientation_update(request, pk):
    Class_Orientation = get_object_or_404(Class_Orientation, pk=pk)
    if request.method == 'POST':
        form = Class_OrientationForm(request.POST, instance=Class_Orientation)
    else:
        form = Class_OrientationForm(instance=Class_Orientation)
    return save_Class_Orientation_form(request, form, 'Class_Orientation/Class_Orientation_update_form.html')


class Class_OrientationList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Class_Orientation


def Class_Orientation_delete(request, pk):
    Class_Orientation = get_object_or_404(Class_Orientation, pk=pk)
    data = dict()
    if request.method == 'POST':
        Class_Orientation.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        Class_Orientation_list = Class_Orientation.objects.all()
        data['html_Class_Orientation_list'] = render_to_string('Class_Orientation/partial_Class_Orientation_list.html', {
            'Class_Orientation_list': Class_Orientation_list
        })
    else:
        context = {'Class_Orientation': Class_Orientation}
        data['html_form'] = render_to_string('Class_Orientation/Class_Orientation_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
