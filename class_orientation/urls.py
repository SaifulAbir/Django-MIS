from django.urls import path
from . import views

app_name = 'peer_education'

urlpatterns = [
    path('add/',views.peer_education_add, name='create_peer_education'),
    path('peer_education_list/',views.PeerEducationList.as_view(), name='peer_education_list'),
    path('peer_education_report/', views.peer_education_report_list, name='peer_education_report_list'),
    path('update/<int:pk>/', views.peer_education_update, name='peer_education_update'),
    path('peer_education_search_list/', views.peer_education_search_list, name = 'peer_education_search_list'),
    path('peer_education_search_list/<export>/', views.peer_education_search_list, name = 'peer_education_search_list_export'),
]