from django.urls import path

from skmembers import views

app_name = 'skmembers'

urlpatterns = [
    path('skmember_add/', views.skmember_profile_view, name='skmember_add'),
    path('skmember_add_for_skleader/', views.skmember_profile_view_skleader, name='skmember_add_for_skleader'),
    path('skmember_list/', views.skmember_list, name = 'skmember_list'),
    path('skmember_list/<export>/', views.skmember_list, name = 'skmember_list_export'),

    path('skmember_list_for_skleader/', views.SkmemberListforSkLeader.as_view(), name = 'skmember_list_for_sk_leader'),
    path('skmember_detail/<int:pk>/', views.SkMemberDetail.as_view(), name = 'skmember_detail'),
    path('skmember_update/<int:pk>', views.skmember_update, name='skmember_update'),
    path('skmember_update_for_skleader/<int:pk>', views.skmember_update_for_skleader, name='skmember_update_for_skleader'),
    path('skmember_school_details_update/', views.skmember_details_update),
]