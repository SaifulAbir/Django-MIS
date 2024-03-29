"""sknf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import handler403
from django.conf.urls import handler500
urlpatterns = [
    path('', include('accounts.urls')),
    path('district/', include('districts.urls')),
    path('division/', include('division.urls')),
    path('', include('school.urls')),
    path('upazilla/', include('upazillas.urls')),
    path('unions/', include('unions.urls')),
    path('headmasters/', include('headmasters.urls')),
    path('skleaders/', include('skleaders.urls')),
    path('skmembers/', include('skmembers.urls')),
    path('topics/', include('topics.urls')),
    path('club_meetings/', include('club_meetings.urls')),
    path('events/', include('events.urls')),
    path('peer_education/',include('class_orientation.urls')),
    path('eduplus_activity/',include('eduplus_activity.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'accounts.views.handler403'
