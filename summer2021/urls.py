"""summer2021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from mySite import views as mySite_views

handler404 = 'mySite.views.handleError404'
handler403 = 'mySite.views.handleError403'
handler400 = 'mySite.views.handleError400'
handler500 = 'mySite.views.handleError500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mySite_views.index),
    path('page/<int:page>/', mySite_views.index),
    path('channels/', mySite_views.channels),
    path('channel/page/<int:page>', mySite_views.channels),
    path('video/<str:id>', mySite_views.video_details),
    path('channel/<str:id>', mySite_views.channel_details),
    path('search-videos', mySite_views.search_videos_result),
    path('search-videos/page/<int:page>', mySite_views.search_videos_result),
    path('search-channels', mySite_views.search_channels_result),
    path('search-channels/page/<int:page>', mySite_views.search_channels_result),
]
