from django.urls import path
from . import views

app_name = 'Class_Orientation'

urlpatterns = [
    path('add/',views.Class_Orientation_create, name='create_Class_Orientation'),
    path('Class_Orientation_list/',views.Class_OrientationList.as_view(), name='Class_Orientation_list'),
    path('delete/<int:pk>/',views.Class_Orientation_delete, name='delete_Class_Orientation'),
    path('update/<int:pk>',views.Class_Orientation_update, name='update_Class_Orientation'),

]