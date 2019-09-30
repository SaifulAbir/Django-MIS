from django.urls import path
from club_meetings import views

app_name = 'club_meetings'


urlpatterns = [
    path('add/', views.club_meeting_add, name='club_meeting_add'),
    path('club_meeting_list/', views.ClubMeetingsList.as_view(), name='club_meeting_list'),
    path('update/<int:pk>/', views.club_meeting_update, name='club_meeting_update'),
    path('club_meeting_detail/<int:pk>/', views.ClubMeetingDetail.as_view(), name = 'club_meeting_detail'),
]