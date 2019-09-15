from django.urls import path

from headmasters.views import headmaster_profile_view

app_name = 'headmasters'

urlpatterns = [
    path('headmaster_add/', headmaster_profile_view, name='headmaster_profile'),
]