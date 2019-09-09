from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import PrettyAuthenticationForm
from .views import index, profile, events, headmaster_home

app_name = 'accounts'

    

urlpatterns = [
    path('dashboard/', index, name = 'dashboard'),
    path('', auth_views.LoginView.as_view(template_name = 'accounts/login.html', authentication_form = PrettyAuthenticationForm, redirect_authenticated_user=True), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/', profile, name='profile'),
    path('events/', events, name='events'),
    path('headmaster_home/', headmaster_home, name='headmaster_home'),



    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),




    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
]

