from django.urls import path
from . import views

app_name = 'districts'

urlpatterns = [
    path('add/', views.district_create, name = 'create_district'),
    path('district_list/', views.DistrictList.as_view(), name = 'district_list'),
    path('delete/<int:pk>/', views.district_delete, name = 'delete_district'),
    path('update/<int:pk>', views.district_update, name = 'update_district')

]