from django.shortcuts import render
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import *
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class NFTOnwersView(LoggingMixin, ListAPIView):
    queryset = NFTOwner.objects.all()
    serializer_class = NFTOwnerSerializer
    permission_classes = [IsAuthenticated]
    search_fiels = ('channel', 'quantity')
    ordering_fields = ('created','updated')
    filterset_fields = ['channel', 'quantity']

    

class NFTOnwerView(LoggingMixin, RetrieveUpdateDestroyAPIView):
    queryset = NFTOwner.objects.all()
    serializer_class = NFTOwnerSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fiels =  ('channel', 'quantity')
    ordering_fields = ('created','updated')
    filterset_fields = ['channel', 'quantity']