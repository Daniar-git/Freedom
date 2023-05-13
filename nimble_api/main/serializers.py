from rest_framework import serializers
from nimble.utils.drf_errors.mixins import FriendlyErrorMessagesMixin
from .models import *

class CommunitySerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'
        
class TagSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class VideoSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class PlaylistSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class ChannelSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'