from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from districts.models import District
from unions.models import Union
from upazillas.models import Upazilla
import unions.strings as union_strings
import resources.strings as common_strings
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
            unions = Union.objects.all()
            paginator = Paginator(unions, 10)
            page = request.GET.get('page')
            try:
                union_list = paginator.page(page)
            except PageNotAnInteger:
                union_list = paginator.page(1)
            except EmptyPage:
                union_list = paginator.page(paginator.num_pages)
            data['html_union_list'] = render_to_string('unions/partial_union_list.html',
                                                          {'union_list': union_list, 'union_strings':union_strings, 'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form, 'union_strings':union_strings, 'common_strings':common_strings}
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
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(UnionList, self).get_context_data(**kwargs)
        unions = Union.objects.all()
        paginator = Paginator(unions, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            union_list = paginator.page(page)
        except PageNotAnInteger:
            union_list = paginator.page(1)
        except EmptyPage:
            union_list = paginator.page(paginator.num_pages)

        context['union_list'] = union_list
        context['common_strings'] = common_strings
        context['union_strings'] = union_strings
        return context

"""class DeleteDistrict(LoginRequiredMixin, generic.DeleteView):

    model = models.District
    success_url = reverse_lazy('districts:district_list')"""

def union_delete(request, pk):
    union = get_object_or_404(Union, pk=pk)
    data = dict()
    if request.method == 'POST':
        union.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        unions = Union.objects.all()
        paginator = Paginator(unions, 10)
        page = request.GET.get('page')
        try:
            union_list = paginator.page(page)
        except PageNotAnInteger:
            union_list = paginator.page(1)
        except EmptyPage:
            union_list = paginator.page(paginator.num_pages)
        data['html_union_list'] = render_to_string('unions/partial_union_list.html', {
            'union_list': union_list, 'union_strings':union_strings, 'common_strings':common_strings
        })
    else:
        context = {'union': union, 'union_strings':union_strings, 'common_strings':common_strings}
        data['html_form'] = render_to_string('unions/union_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districtId = request.GET.get('districtId')
    districtId = int(districtId)
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'unions/district_dropdown_list_options.html', {'districts': districts, 'districtId': districtId})

def load_upazillas(request):
    district_id = request.GET.get('district')
    upazilaId = request.GET.get('upazilaId')
    upazilaId = int(upazilaId)
    upazillas = Upazilla.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'unions/upazilla_dropdown_list_options.html', {'upazillas': upazillas, 'upazilaId':upazilaId})

def load_unions(request):
    upazilla_id = request.GET.get('upazilla')
    unions = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    return render(request, 'unions/union_dropdown_list_options.html', {'unions': unions})

def pagination(request):
    data = dict()
    data['form_is_valid'] = True  # This is just to play along with the existing code
    unions = Union.objects.all()
    paginator = Paginator(unions, 10)
    page = request.GET.get('page')
    try:
        union_list = paginator.page(page)
    except PageNotAnInteger:
        union_list = paginator.page(1)
    except EmptyPage:
        union_list = paginator.page(paginator.num_pages)
    data['html_list'] = render_to_string('unions/partial_union_list.html', {
        'union_list': union_list, 'union_strings':union_strings, 'common_strings':common_strings
    })
    return JsonResponse(data)

