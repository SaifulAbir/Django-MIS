from django.urls import path
from . import views

app_name = 'class_orientation'

urlpatterns = [
    path('add/', views.class_orientation_create, name ='create_class_orientation'),
    path('class_orientation_list/',views.Class_OrientationList.as_view(),name='class_orientation_list'),
    path('delete/<int:pk>/', views.class_orientation_delete,name='delete_class_orientation'),
    path('update/<int:pk>', views.class_orientation_update,name='update_class_orientation'),

]
