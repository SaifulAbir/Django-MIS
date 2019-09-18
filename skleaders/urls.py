from django.urls import path

from skleaders import views

app_name = 'skleaders'

urlpatterns = [
    path('skleader_add/', views.skleader_profile_view, name='skleader_add'),
    path('skleader_list/', views.SkleaderList.as_view(), name = 'skleader_list'),
    path('skleader_detail/<int:pk>/', views.SkleaderDetail.as_view(), name = 'skleader_detail'),
    path('skleader_update/<int:pk>', views.skleader_update, name='skleader_update'),
]