from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from skleaders.models import SkLeaderProfile
from .models import ClassOrientation
from .forms import ClassOrientationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

def class_orientation_add(request):
    profile = SkLeaderProfile.objects.get(user=request.user)
    if request.method == 'POST':
        class_orientation_form = ClassOrientationForm(request.POST, prefix='COF')
        if class_orientation_form.is_valid():
            class_orientation = class_orientation_form.save(commit=False)
            class_orientation.school = profile.school
            class_orientation.save()
            messages.success(request, 'Class Orientation Created!')
            return HttpResponseRedirect("/class_orientation/class_orientation_list/")

    else:
        class_orientation_form = ClassOrientationForm(prefix='COF')

    return render(request, 'class_orientation/classorientation_form.html', {
        'class_orientation_form': class_orientation_form,
    })

class ClubOrientationsList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.ClassOrientation

    def get_queryset(self):
        profile = SkLeaderProfile.objects.get(user=self.request.user)
        queryset = ClassOrientation.objects.filter(school=profile.school)
        return queryset
