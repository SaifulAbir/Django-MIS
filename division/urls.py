
from django.urls import path
from . import views

urlpatterns = [
    path('division_add/', views.division_add, name='division_add'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit',views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
]