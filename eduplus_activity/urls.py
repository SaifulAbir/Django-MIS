from django.urls import path

from . import views

app_name = 'eduplus_activity'


urlpatterns = [
    path('add/', views.edu_plus_activity_add, name='eduplus_activity_add'),
    path('eduplus_activity_list/', views.EduplusActivityList.as_view(), name='eduplus_activity_list'),
    path('update/<int:pk>/', views.edu_plus_activity_update, name='edu_plus_activity_update'),
    path('eduplus_activity_detail/<int:pk>/', views.EduplusActivityDetail.as_view(), name = 'eduplus_activity_detail'),
    path('add_method/', views.method_create, name = 'create_method'),
    path('method_list/', views.EduplusTopicsList.as_view(), name = 'method_list'),
    path('eduplus_activity_report/', views.eduplus_activity_report_list, name='eduplus_activity_report_list'),
    path('delete_method/<int:pk>/', views.method_delete, name = 'delete_method'),
    path('update_method/<int:pk>', views.method_update, name = 'update_method'),
    path('eduplus_activity_search_list/', views.eduplus_activity_search_list, name = 'eduplus_activity_search_list'),
    path('eduplus_activity_search_list/<export>/', views.eduplus_activity_search_list, name = 'eduplus_activity_search_list_export'),
    path('pagination/', views.pagination, name = 'pagination'),
]