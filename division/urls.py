
from django.urls import path
from .import views
urlpatterns = [
    path('', views.division_add, name='division_add'),
    path('division_add/', views.division_add, name='division_add'),
    path('division_list/', views.division_list, name='division_list'),
    path('create/', views.create, name='create'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
    path('update-division', views.update, name='update'),
]