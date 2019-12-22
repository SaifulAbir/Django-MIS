from django.urls import path
from . import views

app_name = 'division'

urlpatterns = [
    path('add/', views.division_create, name = 'create_division'),
    path('division_list/', views.DivisionList.as_view(), name = 'division_list'),
    path('pagination/', views.pagination, name = 'pagination'),
    path('delete/<int:pk>/', views.division_delete, name = 'delete_division'),
    path('update/<int:pk>', views.division_update, name = 'update_division'),

]