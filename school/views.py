from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from accounts.decorators import admin_login_required
from districts.models import District
from headmasters.models import HeadmasterProfile
from school.models import School, SchoolPost
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from unions.models import Union
from upazillas.models import Upazilla
from .forms import SchoolForm, EditSchoolForm, SchoolPostForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import models

@method_decorator(admin_login_required, name='dispatch')
class CreateSchool(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    form_class = SchoolForm
    model = School
    success_message = "School Created!"

@method_decorator(admin_login_required, name='dispatch')
class SchoolUpdate(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    form_class = SchoolForm
    model = models.School
    success_message = "School Updated!"

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
                                                          {'school_list': school_list})
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def school_update(request, pk):
    school = get_object_or_404(School, pk=pk)
    if request.method == 'POST':
        form = SchoolForm(request.POST, instance=school)
    else:
        form = SchoolForm(instance=school)
    return save_school_form(request, form, 'school/school_update_form.html')

@method_decorator(admin_login_required, name='dispatch')
class SchoolList(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    model = models.School

def school_delete(request, pk):
    school = get_object_or_404(School, pk=pk)
    data = dict()
    if request.method == 'POST':
        school.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        school_list = School.objects.all()
        data['html_school_list'] = render_to_string('school/school_list.html', {
            'school_list': school_list
        })
    else:
        context = {'school': school}
        data['html_form'] = render_to_string('school/school_confirm_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def load_districts(request):
    division_id = request.GET.get('division')
    districts = District.objects.filter(division_id=division_id).order_by('name')
    return render(request, 'school/district_dropdown_list_options.html', {'districts': districts})

def load_upazillas(request):
    district_id = request.GET.get('district')
    upazillas = Upazilla.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'school/upazilla_dropdown_list_options.html', {'upazillas': upazillas})

def load_unions(request):
    upazilla_id = request.GET.get('upazilla')
    unions = Union.objects.filter(upazilla_id=upazilla_id).order_by('name')
    return render(request, 'school/union_dropdown_list_options.html', {'unions': unions})

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
                school.save()
                return redirect('school:school_profile', school.id)
            form = EditSchoolForm(instance=school_profile)
        elif 'school_post' in request.POST:
            post_form = SchoolPostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_school = post_form.save(commit=False)
                post_school.school = school_profile
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
        school_post_list = SchoolPost.objects.all()
    except SchoolPost.DoesNotExist:
        school_post_list = None



    return render(request, 'school/school_profile.html', { 'school_profile' : school_profile, 'skleader_profile':skleader_profile, 'profile' : profile, 'headmaster_profile':headmaster_profile,
                                                           'skmember_list': skmember_list, 'form':form, 'upload_head_user':upload_head_user, 'school_post_list':school_post_list,
                                                           'upload_guide_user':upload_guide_user, 'upload_both_user':upload_both_user, 'upload_skleader_user':upload_skleader_user, 'post_form':post_form})

# def image(request,pk):
#     img= HeadmasterProfile.objects.get(pk=pk)
#     return render(request, 'school/school_profile.html'),  {'img': img}

def Sk_leaderApproval(request):
    return render(request, 'school/Sk_leaderApproval.html')


