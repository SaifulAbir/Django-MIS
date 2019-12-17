from django.urls import path
from . import views

app_name = 'class_orientation'

urlpatterns = [
    path('add/',views.class_orientation_add, name='create_class_orientation'),
    path('class_orientation_list/',views.ClubOrientationsList.as_view(), name='class_orientation_list'),
    path('class_orientation_report/', views.class_orientation_report_list, name='class_orientation_report_list'),
    path('update/<int:pk>/', views.class_orientation_update, name='class_orientation_update'),
    path('class_orientation_search_list/', views.class_orientation_search_list, name = 'class_orientation_search_list'),
    path('class_orientation_search_list/<export>/', views.class_orientation_search_list, name = 'class_orientation_search_list_export'),
]