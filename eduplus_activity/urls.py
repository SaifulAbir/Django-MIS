from django.urls import path

from . import views

app_name = 'eduplus_activity'


urlpatterns = [
    path('add/', views.edu_plus_activity_add, name='eduplus_activity_add'),
    path('eduplus_activity_list/', views.EduplusActivityList.as_view(), name='eduplus_activity_list'),
    path('update/<int:pk>/', views.edu_plus_activity_update, name='edu_plus_activity_update'),
    path('eduplus_activity_detail/<int:pk>/', views.EduplusActivityDetail.as_view(), name = 'eduplus_activity_detail'),
]