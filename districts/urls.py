from django.urls import path
from . import views

app_name = 'districts'

urlpatterns = [
    path('add/', views.CreateDistrict.as_view(), name = 'create_district'),
    path('district_list/', views.DistrictList.as_view(), name = 'district_list')
]