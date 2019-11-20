from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts.views import *
from headmasters.views import headmaster_profile_view
from .forms import PrettyAuthenticationForm
from .views import index, profile, events, custom_login, admin_profile_update, headmaster_profile_update, \
    skleader_profile_update, CustomPasswordReset, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, \
    CustomPasswordResetCompleteView, verifyemail, email_verify, bd_map, home_page, search_school_list

app_name = 'accounts'




urlpatterns = [
    path('dashboard/', index, name = 'dashboard'),
    #path('', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = PrettyAuthenticationForm, redirect_authenticated_user=True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/', profile, name='profile'),
    path('events/', events, name='events'),
    path('', custom_login, name='login'),
    path('password_reset/', CustomPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('admin_update/', admin_profile_update, name = 'admin_update'),
    path('headmaster_update/', headmaster_profile_update, name = 'headmaster_update'),
    path('skleader_update/', skleader_profile_update, name = 'skleader_update'),
    path('email_verify/<token>', email_verify, name='email_verify'),

    path('ajax/verifyemail/', verifyemail, name='verifyemail'),
    path('map/', bd_map, name='bd_map'),
    path('home_page/', home_page, name='home_page'),
    path('api/search_school_list/', search_school_list, name='search_school_list'),

]




