from django.urls import path

from skleaders import views

app_name = 'skleaders'

urlpatterns = [
    path('skleader_add/', views.skleader_profile_view, name='skleader_add'),
    path('skleader_list/', views.SkleaderList.as_view(), name = 'skleader_list'),
]