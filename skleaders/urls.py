from django.urls import path

from skleaders import views

app_name = 'skleaders'

urlpatterns = [
    path('skleader_add/', views.skleader_profile_view, name='skleader_add'),
    path('skleader_list/', views.skleader_list, name = 'skleader_list'),
    path('skleader_list/<export>/', views.skleader_list, name = 'skleader_list_export'),
    path('search_skleader_list/', views.skleader_search_list, name = 'search_skleader_list'),
    path('skleader_detail/<int:pk>/', views.SkleaderDetail.as_view(), name = 'skleader_detail'),
    path('skleader_update/<int:pk>', views.skleader_update, name='skleader_update'),
    path('skleader_school_details_update/', views.skleader_details_update),
]