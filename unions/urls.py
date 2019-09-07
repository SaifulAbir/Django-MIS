from django.urls import path
from . import views

app_name = 'unions'

urlpatterns = [
    path('add/', views.union_create, name = 'create_union'),
    path('union_list/', views.UnionList.as_view(), name='union_list'),
    path('delete/<int:pk>/', views.union_delete, name='delete_union'),
    path('update/<int:pk>', views.union_update, name='update_union'),

    path('ajax/load-districts/', views.load_districts, name='ajax_load_districts'),
    path('ajax/load-upazillas/', views.load_upazillas, name='ajax_load_upazillas'),
    path('ajax/load-unions/', views.load_unions, name='ajax_load_unions')

]