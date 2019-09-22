from django.urls import path

from skmembers import views

app_name = 'skmembers'

urlpatterns = [
    path('skmember_add/', views.skmember_profile_view, name='skmember_add'),
    path('skmember_list/', views.SkmemberList.as_view(), name = 'skmember_list'),
    path('skmember_detail/<int:pk>/', views.SkMemberDetail.as_view(), name = 'skmember_detail'),
    path('skmember_update/<int:pk>', views.skmember_update, name='skmember_update'),
]