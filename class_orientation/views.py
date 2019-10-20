from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import headmaster_mentor_skleader_login_required
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from .models import ClassOrientation
from .forms import ClassOrientationForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

@headmaster_mentor_skleader_login_required
def class_orientation_add(request):
    if request.user.is_authenticated and request.user.user_type == 5:
        profile = SkLeaderProfile.objects.get(user=request.user)
    elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
        profile = HeadmasterProfile.objects.get(user=request.user)
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

@headmaster_mentor_skleader_login_required
def class_orientation_update(request, pk):
    class_orientation = get_object_or_404(ClassOrientation, pk=pk)
    if request.method == 'POST':
        class_orientation_form = ClassOrientationForm(request.POST, instance=class_orientation, prefix='COF')
        if class_orientation_form.is_valid():
            class_orientation = class_orientation_form.save(commit=False)
            class_orientation.save()
            messages.success(request, 'Class Orientation Updated!')
            return HttpResponseRedirect("/class_orientation/class_orientation_list/")

    else:
        class_orientation_form = ClassOrientationForm(instance=class_orientation, prefix='COF')

    return render(request, 'class_orientation/classorientation_form.html', {
        'class_orientation_form': class_orientation_form,
    })
