from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('add/', views.CreateSchool.as_view(), name = 'create_school'),
    path('school_list/', views.SchoolList.as_view(), name = 'school_list'),
    path('delete/<int:pk>/', views.school_delete, name = 'delete_school'),
    path('update/<int:pk>', views.SchoolUpdate.as_view(), name = 'update_school'),
    path('details/<int:pk>', views.SchoolDetail.as_view(), name = 'detail_school'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-upazillas/', views.load_upazillas, name='ajax_load_upazillas'),
    path('ajax/load-unions/', views.load_unions, name='ajax_load_unions'),
    path('school_profile/', views.school_profile, name='school_profile'),
    path('Sk_leaderApproval/', views.Sk_leaderApproval, name='Sk_leaderApproval'),
]