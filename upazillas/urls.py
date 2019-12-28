from django.urls import path
from . import views

app_name = 'upazillas'

urlpatterns = [
    path('add/', views.upazilla_create, name = 'create_upazilla'),
    path('upazilla_list/', views.UpazillaList.as_view(), name = 'upazilla_list'),
    path('pagination/', views.pagination, name = 'pagination'),
    path('delete/<int:pk>/', views.upazilla_delete, name = 'delete_upazilla'),
    path('update/<int:pk>', views.upazilla_update, name = 'update_upazilla'),
    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),

]