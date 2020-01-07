from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from districts.models import District
from upazillas.models import Upazilla
from .forms import UpazillaForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models
from . import strings as upazila_strings
from resources import strings as common_strings

def save_upazilla_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            upazillas = Upazilla.objects.all()
            paginator = Paginator(upazillas, 10)
            page = request.GET.get('page')
            try:
                upazila_list = paginator.page(page)
            except PageNotAnInteger:
                upazila_list = paginator.page(1)
            except EmptyPage:
                upazila_list = paginator.page(paginator.num_pages)
            data['html_list'] = render_to_string('upazillas/partial_upazillas_list.html',
                                                          {'upazila_list': upazila_list,'upazila_strings':upazila_strings,
                                                           'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'upazila_strings':upazila_strings,'common_strings':common_strings}
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

@method_decorator(admin_login_required, name='dispatch')
class UpazillaList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.Upazilla
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UpazillaList, self).get_context_data(**kwargs)
        upazilas = Upazilla.objects.all()
        paginator = Paginator(upazilas, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            upazila_list = paginator.page(page)
        except PageNotAnInteger:
            upazila_list = paginator.page(1)
        except EmptyPage:
            upazila_list = paginator.page(paginator.num_pages)

        context['upazila_list'] = upazila_list
        context['upazila_strings'] = upazila_strings
        context['common_strings'] = common_strings
        return context

def upazilla_delete(request, pk):
    upazilla = get_object_or_404(Upazilla, pk=pk)
    data = dict()
    if request.method == 'POST':
        upazilla.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        upazilas = Upazilla.objects.all()
        paginator = Paginator(upazilas, 10)
        page = request.GET.get('page')
        try:
            upazila_list = paginator.page(page)
        except PageNotAnInteger:
            upazila_list = paginator.page(1)
        except EmptyPage:
            upazila_list = paginator.page(paginator.num_pages)
        data['html_list'] = render_to_string('upazillas/partial_upazillas_list.html', {
            'upazila_list': upazila_list,'upazila_strings':upazila_strings,'common_strings':common_strings
        })
    else:
        context = {'upazilla': upazilla,'upazila_strings':upazila_strings,'common_strings':common_strings}
        data['html_form'] = render_to_string('upazillas/upazilla_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districtId = request.GET.get('districtId')
    if districtId:
        districtId = int(districtId)
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'upazillas/district_dropdown_list_options.html',
                  {'districts': districts, 'districtId': districtId})

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    upazilas = Upazilla.objects.all()
    paginator = Paginator(upazilas, 10)
    page = request.GET.get('page')
    try:
        upazila_list = paginator.page(page)
    except PageNotAnInteger:
        upazila_list = paginator.page(1)
    except EmptyPage:
        upazila_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('division/partial_division_list.html', {
        'upazila_list': upazila_list,'upazila_strings':upazila_strings,'common_strings':common_strings
    })
    return JsonResponse(data)