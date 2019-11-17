from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('add/', views.CreateSchool.as_view(), name = 'create_school'),
    path('export/', views.export, name = 'export_school'),
    path('school_list/', views.school_list, name = 'school_list'),
    path('school_list/<export>/', views.school_list, name = 'school_list_export'),

    path('delete/<int:pk>/', views.school_delete, name = 'delete_school'),
    path('update/<int:pk>', views.SchoolUpdate.as_view(), name = 'update_school'),
    path('details/<int:pk>', views.SchoolDetail.as_view(), name = 'detail_school'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-upazillas/', views.load_upazillas, name='ajax_load_upazillas'),
    path('ajax/load-unions/', views.load_unions, name='ajax_load_unions'),
    path('<int:pk>/', views.school_profile, name='school_profile'),
    path('school_profile_homepage/', views.school_profile, name='school_profile'),
    path('school_post_detail/<int:pk>', views.school_post_detail_view, name='school_post_detail_view'),
    path('school_post_delete/<int:pk>', views.school_post_delete, name='school_post_delete'),
    path('Sk_leaderApproval/', views.Sk_leaderApproval, name='Sk_leaderApproval'),
]