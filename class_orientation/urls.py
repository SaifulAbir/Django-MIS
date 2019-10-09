from django.urls import path
from . import views

app_name = 'class_orientation'

urlpatterns = [
    path('add/',views.class_orientation_add, name='create_class_orientation'),
    path('class_orientation_list/',views.ClubOrientationsList.as_view(), name='class_orientation_list'),

]