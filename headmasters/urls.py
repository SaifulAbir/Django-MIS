from django.urls import path

from headmasters import views


app_name = 'headmasters'

urlpatterns = [
    path('headmaster_add/', views.headmaster_profile_view, name='headmaster_profile'),
    path('headmaster_list/', views.HeadmasterList.as_view(), name = 'headmaster_list'),
    path('headmaster_detail/<int:pk>/', views.HeadmasterDetail.as_view(), name = 'headmaster_detail'),
    path('headmaster_update/<int:pk>', views.headmaster_update, name='headmaster_update'),
]