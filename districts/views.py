from django.shortcuts import render
from .forms import DistrictForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models


class CreateDistrict(LoginRequiredMixin, generic.CreateView):

    model = models.District
    form_class = DistrictForm

class DistrictList(LoginRequiredMixin, generic.ListView):

    model = models.District
