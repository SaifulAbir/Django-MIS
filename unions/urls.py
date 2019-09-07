from django.urls import path
from . import views

app_name = 'unions'

urlpatterns = [
    path('add/', views.union_create, name = 'create_union'),
    path('union_list/', views.UnionList.as_view(), name = 'union_list'),
    path('delete/<int:pk>/', views.union_delete, name = 'delete_union'),
    path('update/<int:pk>', views.union_update, name = 'update_union')

]