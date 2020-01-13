from django.urls import path

from headmasters import views


app_name = 'headmasters'

urlpatterns = [
    path('headmaster_add/', views.headmaster_profile_view, name='headmaster_profile'),
    path('headmaster_list/', views.headmaster_list, name = 'headmaster_list'),
    path('search_headmaster_list/', views.headmaster_search_list, name = 'search_headmaster_list'),
    path('headmaster_list/<export>/', views.headmaster_list, name = 'headmaster_list_export'),

    path('headmaster_detail/<int:pk>/', views.HeadmasterDetail.as_view(), name = 'headmaster_detail'),
    path('headmaster_update/<int:pk>', views.headmaster_update, name='headmaster_update'),
    path('headmaster_school_details_update/', views.headermaster_school_details_update),
]