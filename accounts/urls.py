from django.urls import path
from django.contrib.auth import views as auth_views

from headmasters.views import headmaster_profile_view
from .forms import PrettyAuthenticationForm
from .views import index, profile, events, custom_login, admin_profile_update, headmaster_profile_update, \
    skleader_profile_update

app_name = 'accounts'

    

urlpatterns = [
    path('dashboard/', index, name = 'dashboard'),
    #path('', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = PrettyAuthenticationForm, redirect_authenticated_user=True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/', profile, name='profile'),
    path('events/', events, name='events'),

    path('', custom_login, name='login'),


    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),

    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('admin_update/', admin_profile_update, name = 'admin_update'),
    path('headmaster_update/', headmaster_profile_update, name = 'headmaster_update'),
    path('skleader_update/', skleader_profile_update, name = 'skleader_update'),



]




