from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts.views import *
from headmasters.views import headmaster_profile_view
from .forms import PrettyAuthenticationForm
from .views import index, events, custom_login, admin_profile_update, headmaster_profile_update, \
    skleader_profile_update, search_school_list, load_previous_school, load_previous_eiin, load_previous_user, home_login

app_name = 'accounts'




urlpatterns = [
    path('dashboard/', index, name = 'dashboard'),
    #path('', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = PrettyAuthenticationForm, redirect_authenticated_user=True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('events/', events, name='events'),
    path('', custom_login, name='login'),
    path('login/', home_login, name='home_login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('admin_update/', admin_profile_update, name = 'admin_update'),
    path('headmaster_update/', headmaster_profile_update, name = 'headmaster_update'),
    path('skleader_update/', skleader_profile_update, name = 'skleader_update'),
    path('api/search_school_list/', search_school_list, name='search_school_list'),
    path('load_previous_schools/', load_previous_school, name='load_previous_schools'),
    path('load_previous_eiins/', load_previous_eiin, name='load_previous_eiins'),
    path('load_previous_divisions/', load_previous_division, name='load_previous_divisions'),
    path('load_previous_districts/', load_previous_district, name='load_previous_districts'),
    path('load_previous_upazillas/', load_previous_upazilla, name='load_previous_upazillas'),
    path('load_previous_unions/', load_previous_union, name='load_previous_unions'),
    path('load_previous_users/', load_previous_user, name='load_previous_users'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('load_previous_headmaster_mobile/', load_previous_headmaster_mobile, name='load_previous_headmaster_mobile'),
<<<<<<< HEAD
    path('load_previous_headmaster/', load_previous_headmaster, name='load_previous_headmaster'),
    path('load_previous_skleader/', load_previous_skleader, name='load_previous_skleader'),
    path('load_previous_skmember/', load_previous_skmember, name='load_previous_skmember'),
=======
    path('load_previous_skleader_mobile/', load_previous_skleader_mobile, name='load_previous_skleader_mobile'),
>>>>>>> feature/admin_skleader
=======
    path('load_previous_skmember_mobile/', load_previous_skmember_mobile, name='load_previous_skmember_mobile'),
>>>>>>> features/admin_skmember
=======
    path('load_previous_headmaster_mobile/', load_previous_headmaster_mobile, name='load_previous_headmaster_mobile'),
    path('load_previous_skleader_mobile/', load_previous_skleader_mobile, name='load_previous_skleader_mobile'),
    path('load_previous_headmaster/', load_previous_headmaster, name='load_previous_headmaster'),
    path('load_previous_skleader/', load_previous_skleader, name='load_previous_skleader'),
    path('load_previous_skmember/', load_previous_skmember, name='load_previous_skmember'),
    path('load_previous_skmember_mobile/', load_previous_skmember_mobile, name='load_previous_skmember_mobile'),
>>>>>>> feature/hotfix_0.9

]




