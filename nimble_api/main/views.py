from django.shortcuts import render
from .models import *
from marketplace.models import NFTOwner
from .serializers import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from nimble.user.models import User
from rest_framework.generics import *
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
# Create your views here.


class CommunitiesView(LoggingMixin, ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('name',)
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)
    

class CommunityView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('name',)
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)


class TagsView(LoggingMixin, ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    search_fields = ('name', )
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)


class TagView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('name', )
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)


class VideosView(LoggingMixin, ListCreateAPIView):
    queryset = Video.objects.all().order_by('-created')
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination
    search_fields = ('title', 'description')
    ordering_fields = ('created', 'updated', 'views')
    filterset_fields = ['title', 'description', 'views', 'category', 'is_private', 'channel']

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(is_private=False)
        if not user.is_authenticated:
            return queryset
        else:
            if not NFTOwner.objects.filter(user=user).exists():
                return queryset
            channels = NFTOwner.objects.filter(user=user).values_list('channel', flat=True)
            extra_query = self.queryset.filter(channel__in=channels)
            queryset = queryset | extra_query
            return queryset


class VideoView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('title', 'description')
    ordering_fields = ('created', 'updated', 'views')
    filterset_fields = ['title', 'description', 'views', 'category', 'is_private']


class ChannelVideosView(LoggingMixin, ListAPIView):
    queryset = Video.objects.all().order_by('-created')
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('title', 'description')
    ordering_fields = ('created', 'updated', 'views')
    filterset_fields = ['title', 'description', 'views', 'category', 'is_private']

    def get_queryset(self):
        channel = self.kwargs['channel_id']
        user = self.request.user
        queryset = self.queryset.filter(is_private=False, channel=channel)
        if not user.is_authenticated:
            return queryset
        else:
            if NFTOwner.objects.filter(channel=channel, user=user).exists():
                extra_query = self.queryset.filter(is_private=True, channel=channel)
                queryset = queryset | extra_query
            return queryset


class PlaylistsView(LoggingMixin, ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('name', 'description')
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)


class PlaylistView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('name', 'description')
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)


class ChannelsView(LoggingMixin, ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ('name', 'description')
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)

    def create(self, request):
        data = request.data.copy()
        if not ('user' in data):
            data['user'] = User.pk
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def get_queryset(self):
    #     channel_id = self.kwargs['channel_id']
    #     user_id = self.request.user
    #     queryset = self.queryset.filter(is_private=False, channel=channel_id)
    #     if not user_id.is_authenticated:
    #         return queryset
    #     else:
    #         if NFTOwner.objects.filter(channel=channel_id, user=user_id):
    #             extra_query = self.queryset.filter(is_private=True, channel=channel_id)
    #             queryset = queryset | extra_query
    #         return queryset


class ChannelView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('name', 'description')
    ordering_fields = ('created', 'updated')
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(name=self.request.user)

