import base64
import uuid
import school.strings as school_strings
from resources import strings as common_strings
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.base import ContentFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from sknf.helper import check_child_data_exist_on_delete
from accounts.decorators import admin_login_required
from districts.models import District
from headmasters.models import HeadmasterProfile
from school.models import School, SchoolPost
from school.resources import SchoolResource
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from unions.models import Union
from upazillas.models import Upazilla
from .forms import SchoolForm, EditSchoolForm, SchoolPostForm, SchoolUpdatePostForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

@method_decorator(admin_login_required, name='dispatch')
class CreateSchool(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    form_class = SchoolForm
    model = School
    success_message = school_strings.SCHOOL_CREATED_MSG

@method_decorator(admin_login_required, name='dispatch')
class SchoolUpdate(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    form_class = SchoolForm
    model = models.School
    success_message = school_strings.SCHOOL_UPDATED_MSG

@method_decorator(admin_login_required, name='dispatch')
class SchoolDetail(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    context_object_name = "school_detail"
    model = models.School
    template_name = 'school/school_detail.html'

def save_school_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            school_list = School.objects.all()
            data['html_school_list'] = render_to_string('school/partial_school_list.html',
                                                          {'school_list': school_list,'school_strings':school_strings,'common_strings':common_strings})
        else:
            data['form_is_valid'] = False
    context = {'form': form,'school_strings':school_strings,'common_strings':common_strings}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
    else:
        form = SchoolForm(instance=school)
    return save_school_form(request, form, 'school/school_update_form.html')


@admin_login_required
def school_list(request, export='null'):
    qs=School.objects.all()
    name= request.GET.get('name_contains')
    school_id= request.GET.get('school_id_contains')
    division= request.GET.get('division_contains')
    district= request.GET.get('district_contains')
    upazilla=  request.GET.get('upazilla_contains')
    union =  request.GET.get('union_contains')
    if name !='' and name is not None:
        qs = qs.filter(name__icontains=name)
    if school_id != '' and school_id is not None:
        qs = qs.filter(school_id__icontains=school_id)
    if division !='' and division is not None:
        qs = qs.filter(division__name__icontains=division)
    if district !='' and district is not None:
        qs = qs.filter(district__name__icontains=district)
    if upazilla != '' and upazilla is not None:
        qs = qs.filter(upazilla__name__icontains=upazilla)
    if union !='' and union is not None:
        qs = qs.filter(union__name__icontains=union)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if export != 'export':
        return render(request, 'school/school_list.html', {'queryset': queryset,'name':name,'school_id':school_id,'division':division,
                                                       'district':district,'upazilla':upazilla,'union':union,'school_strings':school_strings,'common_strings':common_strings})
    else:
        resource = SchoolResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="school_list.csv"'
        return response

def school_list_search_list(request, export='null'):
    data = dict()
    qs = School.objects.all()
    name = request.GET.get('name_contains')
    school_id = request.GET.get('school_id_contains')
    division = request.GET.get('division_contains')
    district = request.GET.get('district_contains')
    upazilla = request.GET.get('upazilla_contains')
    union = request.GET.get('union_contains')
    if name != '' and name is not None:
        qs = qs.filter(name__icontains=name)
    if school_id != '' and school_id is not None:
        qs = qs.filter(school_id__icontains=school_id)
    if division != '' and division is not None:
        qs = qs.filter(division__name__icontains=division)
    if district != '' and district is not None:
        qs = qs.filter(district__name__icontains=district)
    if upazilla != '' and upazilla is not None:
        qs = qs.filter(upazilla__name__icontains=upazilla)
    if union != '' and union is not None:
        qs = qs.filter(union__name__icontains=union)

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    if name == '' and school_id == '' and division == '' and district == '' and upazilla == '' and union=='':
        queryset = None
    data['form_is_valid'] = True
    data['html_list'] = render_to_string('school/partial_school_list.html',
                                                {'queryset': queryset,'school_strings':school_strings,'common_strings':common_strings})

    if export != 'export':
        return JsonResponse(data)
    else:
        resource = SchoolResource()
        dataset = resource.export(qs)
        response = HttpResponse(dataset.csv, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="school_list.csv"'
        return response






def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    data = dict()
    if request.method == 'POST':
        status = check_child_data_exist_on_delete(school)
        data['status'] = status
        data['form_is_valid'] = True  # This is just to play along with the existing code
        school_list = School.objects.all()
        data['html_school_list'] = render_to_string('school/partial_school_list.html', {
            'queryset': school_list,'school_strings':school_strings,'common_strings':common_strings
        })
    else:
        context = {'school': school,'school_strings':school_strings,'common_strings':common_strings}
        data['html_form'] = render_to_string('school/school_confirm_delete.html',
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
    return render(request, 'school/district_dropdown_list_options.html', {'districts': districts, 'districtId': districtId })

def load_upazillas(request):
    district_id = request.GET.get('district')
    upazilaId = request.GET.get('upazilaId')
    if upazilaId:
        upazilaId = int(upazilaId)
    upazillas = Upazilla.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'school/upazilla_dropdown_list_options.html', {'upazillas': upazillas, 'upazilaId':upazilaId})

def load_unions(request):
    upazilla_id = request.GET.get('upazilla')
    unionId = request.GET.get('unionId')
    if unionId:
        unionId = int(unionId)
    unions = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    return render(request, 'school/union_dropdown_list_options.html', {'unions': unions, 'unionId':unionId})

def school_profile(request, pk):
    school_profile = get_object_or_404(School, pk=pk)
    if request.user.is_authenticated:
        try:
            upload_head_user = HeadmasterProfile.objects.filter(school__id=pk, user__user_type=2, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            upload_head_user = None
        try:
            upload_guide_user = HeadmasterProfile.objects.filter(school__id=pk, user__user_type=3, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            upload_guide_user = None
        try:
            upload_both_user = HeadmasterProfile.objects.filter(school__id=pk, user__user_type=4, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            upload_both_user = None
        try:
            upload_skleader_user = SkLeaderProfile.objects.filter(school__id=pk, user__user_type=5, user=request.user).latest('school__id')
        except SkLeaderProfile.DoesNotExist:
            upload_skleader_user = None
    else:
        upload_head_user = None
        upload_guide_user = None
        upload_both_user = None
        upload_skleader_user = None
    try:
        headmaster_profile = HeadmasterProfile.objects.filter(school__id=pk, user__user_type=2).latest('school__id')
    except HeadmasterProfile.DoesNotExist:
        headmaster_profile = None
    try:
        skleader_profile = SkLeaderProfile.objects.filter(school__id=pk, user__user_type=5).latest('school__id')
    except SkLeaderProfile.DoesNotExist:
        skleader_profile = None

    if request.user.is_authenticated and request.user.user_type == 1:
        profile=request.user
    elif request.user.is_authenticated and request.user.user_type == 2:
        try:
            profile = HeadmasterProfile.objects.filter(school__id=pk, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            profile = None
    elif request.user.is_authenticated and request.user.user_type == 3:
        try:
            profile = HeadmasterProfile.objects.filter(school__id=pk, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            profile = None
    elif request.user.is_authenticated and request.user.user_type == 4:
        try:
            profile = HeadmasterProfile.objects.filter(school__id=pk, user=request.user).latest('school__id')
        except HeadmasterProfile.DoesNotExist:
            profile = None

    elif request.user.is_authenticated and request.user.user_type == 5:
        try:
            profile = SkLeaderProfile.objects.get(school__id=pk, user=request.user)
        except SkLeaderProfile.DoesNotExist:
            profile = None
    else:
        profile = None
            
    if request.method == 'POST':
        form = EditSchoolForm(instance=school_profile)
        post_form = SchoolPostForm()
        if 'one_picture' in request.POST:
            form = EditSchoolForm(request.POST, request.FILES, instance=school_profile)
            if form.is_valid():
                school = form.save(commit=False)
                # image cropping code start here
                img_base64 = form.cleaned_data.get('cover_image_base64')
                if img_base64:
                    format, imgstr = img_base64.split(';base64,')
                    ext = format.split('/')[-1]
                    filename = str(uuid.uuid4()) + '-school_post.' + ext
                    data = ContentFile(base64.b64decode(imgstr), name=filename)
                    school.image.save(filename, data, save=True)
                    school.image = 'images/' + filename
                # end of image cropping code
                school.save()
                return redirect('school:school_profile', school.id)
            form = EditSchoolForm(instance=school_profile)
        elif 'school_post' in request.POST:
            post_form = SchoolPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_school = post_form.save(commit=False)
                post_school.school = school_profile
                # image cropping code start here
                img_base64 = post_form.cleaned_data.get('image_base64')
                if img_base64:
                    format, imgstr = img_base64.split(';base64,')
                    ext = format.split('/')[-1]
                    filename = str(uuid.uuid4()) + '-school_post.' + ext
                    data = ContentFile(base64.b64decode(imgstr), name=filename)
                    post_school.post_image.save(filename, data, save=True)
                    post_school.post_image = 'images/' + filename
                # end of image cropping code
                post_school.save()
                return redirect('school:school_profile', school_profile.id)
            post_form = SchoolPostForm()
    else:
        form = EditSchoolForm(instance=school_profile)
        post_form = SchoolPostForm()

    try:
        skmember_list = SkMemberProfile.objects.filter(school__id__in=[pk, ])
    except SkMemberProfile.DoesNotExist:
        skmember_list = None

    try:
        skleader_list = SkLeaderProfile.objects.filter(school__id__in=[pk, ])
    except SkMemberProfile.DoesNotExist:
        skleader_list = None

    try:
        school_post_list = SchoolPost.objects.filter(school__id=school_profile.id)
    except SchoolPost.DoesNotExist:
        school_post_list = None



    return render(request, 'school/school_profile.html', { 'school_profile' : school_profile, 'skleader_list' : skleader_list, 'profile' : profile, 'headmaster_profile':headmaster_profile,
                                                           'skmember_list': skmember_list, 'form':form, 'upload_head_user':upload_head_user, 'school_post_list':school_post_list,
                                                           'upload_guide_user':upload_guide_user, 'upload_both_user':upload_both_user, 'upload_skleader_user':upload_skleader_user,
                                                           'post_form':post_form, 'school_strings':school_strings, 'common_strings':common_strings})


def school_post_detail_view(request, pk):
    post_detail = get_object_or_404(SchoolPost, pk=pk)
    try:
        headmaster_profile = HeadmasterProfile.objects.filter(school__id=post_detail.school.id, user__user_type=2).latest('school__id')
    except HeadmasterProfile.DoesNotExist:
        headmaster_profile = None
    try:
        skleader_profile = SkLeaderProfile.objects.filter(school__id=post_detail.school.id, user__user_type=5).latest('school__id')
    except SkLeaderProfile.DoesNotExist:
        skleader_profile = None
    return render(request, "school/school_post_detail.html", {'post_detail': post_detail, 'headmaster_profile': headmaster_profile, 'skleader_profile':skleader_profile,'school_strings':school_strings,'common_strings':common_strings})

# def image(request,pk):
#     img= HeadmasterProfile.objects.get(pk=pk)
#     return render(request, 'school/school_profile.html'),  {'img': img}


def export(request):
    resource = SchoolResource()
    dataset = resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="school_list.csv"'
    return response

def school_post_delete(request, pk):
    school_post = get_object_or_404(SchoolPost, pk=pk)
    data = dict()
    if request.method == 'POST':
        school_post.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        school_post_list = SchoolPost.objects.all()
        data['html_school_post_list'] = render_to_string('school/partial_school_post_list.html', {
            'school_post_list': school_post_list,'school_strings':school_strings,'common_strings':common_strings
        })
    else:
        context = {'school_post_delete': school_post,'school_strings':school_strings,'common_strings':common_strings}
        data['html_form'] = render_to_string('school/schoolpost_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def school_post_update(request, pk):
    data = dict()
    school_post = get_object_or_404(SchoolPost, pk=pk)
    if request.method == 'POST':
        form = SchoolUpdatePostForm(request.POST, request.FILES, instance=school_post)
        if form.is_valid():
            update_post = form.save(commit=False)
            # image cropping code start here
            img_base = form.cleaned_data.get('image_base')
            if img_base:
                format, imgstr = img_base.split(';base64,')
                ext = format.split('/')[-1]
                filename = str(uuid.uuid4()) + '-school_post.' + ext
                data = ContentFile(base64.b64decode(imgstr), name=filename)
                update_post.post_image.save(filename, data, save=True)
                update_post.post_image = 'images/' + filename
            # end of image cropping code
            update_post.save()
            school_post_list = SchoolPost.objects.all()
            return JsonResponse({'data':'ok'})

        else:
            data['form_is_valid'] = False
    else:
        form = SchoolUpdatePostForm(instance=school_post)
        context = {'post_form': form, 'school_strings':school_strings,'common_strings':common_strings}
        data['html_form'] = render_to_string('school/school_post_update_form.html', context, request=request)
    return JsonResponse(data)



