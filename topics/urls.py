from django.urls import path
from . import views

app_name = 'topics'

urlpatterns = [
    path('add/', views.topics_create, name = 'create_topics'),
    path('topics_list/', views.TopicsList.as_view(), name = 'topics_list'),
    path('delete/<int:pk>/', views.topics_delete, name = 'delete_topics'),
    path('update/<int:pk>', views.topics_update, name = 'update_topics'),
    ]