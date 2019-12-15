from django.urls import path

from . import views

app_name = 'eduplus_activity'


urlpatterns = [
    path('add/', views.edu_plus_activity_add, name='eduplus_activity_add'),
    path('eduplus_activity_list/', views.EduplusActivityList.as_view(), name='eduplus_activity_list'),
    path('update/<int:pk>/', views.edu_plus_activity_update, name='edu_plus_activity_update'),
    path('eduplus_activity_detail/<int:pk>/', views.EduplusActivityDetail.as_view(), name = 'eduplus_activity_detail'),
    path('add_eduplus_topics/', views.eduplus_topics_create, name = 'create_eduplus_topics'),
    path('eduplus_topics_list/', views.EduplusTopicsList.as_view(), name = 'eduplus_topics_list'),
    path('eduplus_activity_report/', views.eduplus_activity_report_list, name='eduplus_activity_report_list'),
    path('delete_eduplus_topics/<int:pk>/', views.eduplus_topics_delete, name = 'delete_eduplus_topics'),
    path('update_eduplus_topics/<int:pk>', views.eduplus_topics_update, name = 'eduplus_update_topics'),
    path('eduplus_activity_search_list/', views.eduplus_activity_search_list, name = 'eduplus_activity_search_list'),
    path('eduplus_activity_search_list/<export>/', views.eduplus_activity_search_list, name = 'eduplus_activity_search_list_export'),
]