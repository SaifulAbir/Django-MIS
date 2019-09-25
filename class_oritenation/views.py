from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from class_oritenation.models import Class_Orientation
from .forms import Class_OrientationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from class_oritenation import models


def save_class_orientation_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            class_orientation_list = Class_Orientation.objects.all()
            data['html_class_orientation_list'] = render_to_string('class_orientation/partial_class_orientation_list.html',
                                                          {'class_orientation_list': class_orientation_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def class_orientation_create(request):
    data = dict()

    if request.method == 'POST':
        form = Class_OrientationFrom(request.POST)
    else:
        form = Class_OrientationFrom()
    return save_class_orientation_form(request, form, 'class_orientation/class_orientation_form.html')

def class_orientation_update(request, pk):
    class_orientation = get_object_or_404(Class_Orientation, pk=pk)
    if request.method == 'POST':
        form = Class_OrientationFrom(request.POST, instance=class_orientation)
    else:
        form = Class_OrientationFrom(instance=class_orientation)
    return save_class_orientation_form(request, form, 'class_orientation/class_orientation_update_form.html')


class Class_OrientationList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Class_Orientation



def class_orientation_delete(request, pk):
    class_orientation = get_object_or_404(Class_Orientation, pk=pk)
    data = dict()
    if request.method == 'POST':
        class_orientation.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        class_orientation_list = Class_Orientation.objects.all()
        data['html_class_orientation_list'] = render_to_string('class_orientation/partial_class_orientation_list.html', {
            'class_orientation_list': class_orientation_list
        })
    else:
        context = {'class_orientation': class_orientation}
        data['html_form'] = render_to_string('class_orientation/class_orientation_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)