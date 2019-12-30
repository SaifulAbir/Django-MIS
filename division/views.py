from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
import division.strings as division_strings
from resources import strings as common_strings
from accounts.decorators import admin_login_required
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
            divisions = Division.objects.all()
            paginator = Paginator(divisions, 10)
            page = request.GET.get('page')
            try:
                division_list = paginator.page(page)
            except PageNotAnInteger:
                division_list = paginator.page(1)
            except EmptyPage:
                division_list = paginator.page(paginator.num_pages)
            data['html_list'] = render_to_string('division/partial_division_list.html',
                                                          {'division_list': division_list, 'division_strings':division_strings, 'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'division_strings':division_strings, 'common_strings':common_strings}
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

@method_decorator(admin_login_required, name='dispatch')
class DivisionList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Division
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DivisionList, self).get_context_data(**kwargs)
        divisions = Division.objects.all()
        paginator = Paginator(divisions, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            division_list = paginator.page(page)
        except PageNotAnInteger:
            division_list = paginator.page(1)
        except EmptyPage:
            division_list = paginator.page(paginator.num_pages)

        context['division_list'] = division_list
        context['common_strings'] = common_strings
        context['division_strings'] = division_strings
        return context

def division_delete(request, pk):
    division = get_object_or_404(Division, pk=pk)
    data = dict()
    if request.method == 'POST':
        division.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        divisions = Division.objects.all()
        paginator = Paginator(divisions, 10)
        page = request.GET.get('page')
        try:
            division_list = paginator.page(page)
        except PageNotAnInteger:
            division_list = paginator.page(1)
        except EmptyPage:
            division_list = paginator.page(paginator.num_pages)
        data['html_list'] = render_to_string('division/partial_division_list.html', {
            'division_list': division_list, 'division_strings':division_strings, 'common_strings':common_strings
        })
    else:
        context = {'division': division, 'division_strings':division_strings, 'common_strings':common_strings}
        data['html_form'] = render_to_string('division/division_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    divisions = Division.objects.all()
    paginator = Paginator(divisions, 10)
    page = request.GET.get('page')
    try:
        division_list = paginator.page(page)
    except PageNotAnInteger:
        division_list = paginator.page(1)
    except EmptyPage:
        division_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('division/partial_division_list.html', {
        'division_list': division_list, 'division_strings':division_strings, 'common_strings':common_strings
    })
    return JsonResponse(data)
