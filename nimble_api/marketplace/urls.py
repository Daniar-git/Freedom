from django.urls import path, include
from marketplace import views
from .views import *
from .serializers import *

urlpatterns = [
    path('nft_owners/', NFTOnwersView.as_view()),
    path('nft_owners/<int:pk>/', NFTOnwerView.as_view()),
]
