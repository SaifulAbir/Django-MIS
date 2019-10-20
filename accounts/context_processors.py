from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from headmasters.models import HeadmasterProfile
from school.models import School
from skleaders.models import SkLeaderProfile


def sidebar_context(request):
    if request.user.is_authenticated:
        try:
            if request.user.is_authenticated and request.user.user_type == 1:
                h_profile=None
            elif request.user.is_authenticated and request.user.user_type == 2 or request.user.user_type == 3 or request.user.user_type == 4:
                h_profile = HeadmasterProfile.objects.get(user=request.user)
            elif request.user.is_authenticated and request.user.user_type == 5:
                h_profile = SkLeaderProfile.objects.get(user=request.user)
            else:
                h_profile = None
        except HeadmasterProfile.DoesNotExist:
            h_profile=None
        if h_profile is not None:
            school_profile = get_object_or_404(School, pk=h_profile.school.id)
        else:
            school_profile=None
        if school_profile is not None:
            try:
                headmaster_profile = HeadmasterProfile.objects.filter(school__id=school_profile.id, user__user_type=2).latest('school__id')
            except HeadmasterProfile.DoesNotExist:
                headmaster_profile = None
        else:
            headmaster_profile=None
        if school_profile is not None:
            try:
                skleader_profile = SkLeaderProfile.objects.filter(school__id=school_profile.id, user__user_type=5).latest('school__id')
            except SkLeaderProfile.DoesNotExist:
                skleader_profile = None
        else:
            skleader_profile=None
        if request.user.is_authenticated and request.user.user_type == 1:
            profile = request.user
        elif request.user.is_authenticated and request.user.user_type == 2:
            profile = HeadmasterProfile.objects.get(user=request.user)
        elif request.user.is_authenticated and request.user.user_type == 3:
            profile = HeadmasterProfile.objects.get(user=request.user)
        elif request.user.is_authenticated and request.user.user_type == 4:
            profile = HeadmasterProfile.objects.get(user=request.user)
        elif request.user.is_authenticated and request.user.user_type == 5:
            profile = SkLeaderProfile.objects.get(user=request.user)
        else:
            profile = None
        return {
            'profile': profile, 'headmaster_profile':headmaster_profile, 'skleader_profile':skleader_profile
        }
    else:
        return {
            'profile': None, 'headmaster_profile':None, 'skleader_profile':None
        }