from django.urls import path, include
from main import views
from .views import *
from .serializers import *
from rest_framework.generics import *

urlpatterns = [
    path('communities/', CommunitiesView.as_view()),
    path('communities/<int:pk>/', CommunityView.as_view()),
    path('tags/', TagsView.as_view()),
    path('tags/<int:pk>/', TagView.as_view()),
    path('videos/', VideosView.as_view()),
    path('videos/<int:pk>/', VideoView.as_view()),
    path('playlists/', PlaylistsView.as_view()),
    path('playlists/<int:pk>/', PlaylistView.as_view()),
    path('channels/', ChannelsView.as_view()),
    path('channels/<int:pk>/', ChannelView.as_view()),
    path('channel/<int:channel_id>/videos/', ChannelVideosView.as_view()),
]
