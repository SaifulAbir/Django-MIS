from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('create_event/', views.create_event, name = 'create_event'),
    path('api/add_event/', views.add_event, name = 'add_event'),
    path('api/update_event/', views.update_event, name = 'update_event'),
    path('api/delete_event/', views.delete_event, name = 'delete_event'),
    path('event_list/', views.event_list, name='event_list'),

]