from rest_framework import serializers
from nimble.utils.drf_errors.mixins import FriendlyErrorMessagesMixin
from .models import *

class NFTOwnerSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = NFTOwner
        fields = '__all__'