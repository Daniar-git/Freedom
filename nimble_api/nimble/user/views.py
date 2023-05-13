from django.contrib.messages.views import SuccessMessageMixin
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.hashers import make_password
from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import PasswordResetView
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import random
import string

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework_tracking.mixins import LoggingMixin
from rest_framework.parsers import FileUploadParser
from rest_framework import generics, views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from dj_rest_auth.views import UserDetailsView, LoginView

from .models import *
from .serializers import *

# Metamask
class UserView(UserDetailsView):
    """
    patch:
    Update user

    ---

    get:
    Return user

    ---

    put:
    Update user

    ---
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = PageNumberPagination
    parser_class = (FileUploadParser)


class FacebookLogin(LoggingMixin, SocialLoginView):
    """
    post:
    Facebook authentication

    ---
        parameters:

        - name: access_token
          description: "oauth_token" (OAuth1) or access token (OAuth2)
          required: true
          type: string

        - name: code
          description: App ID
          required: false
          type: string
    """
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(LoggingMixin, SocialLoginView):
    """
    post:
    Google authentication

    ---
        parameters:

        - name: access_token
          description: "oauth_token" (OAuth1) or access token (OAuth2)
          required: true
          type: string

        - name: code
          description: Client ID
          required: false
          type: string
    """
    adapter_class = GoogleOAuth2Adapter


class PasswordReset(LoggingMixin, SuccessMessageMixin, PasswordResetView):
    """
    post:
    User Password Reset

    ---
        parameters:

        - name: email
          description: User email
          required: true
          type: string
    """
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer


class CreateSuperuserView(LoggingMixin, views.APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            return Response({
                'status': 'error'
            }, status=status.HTTP_400_BAD_REQUEST)
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user = User.objects.create(email=email, username=email, password=make_password(password), is_staff=True,
                                   is_superuser=True, type=0)

        subject = 'New user'
        html_message = render_to_string('email/new_user.html', {'context': {'email': email, 'password': password}})
        plain_message = strip_tags(html_message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class UsersView(LoggingMixin, generics.ListAPIView):
    """
    get:
    Return all users

    ---
    """
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all().order_by('pk')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ('email', 'first_name', 'last_name')


class UserDetailView(LoggingMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    patch:
    Update user

    ---
        parameters:

        - name: id
          description: User id
          required: true
          type: int

    get:
    Return user

    ---
        parameters:

        - name: id
          description: User id
          required: true
          type: int

    put:
    Update user

    ---
        parameters:

        - name: id
          description: User id
          required: true
          type: int

    delete:
    Delete user

    ---
        parameters:

        - name: id
          description: User id
          required: true
          type: int
    """
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        user = get_object_or_404(User, email=self.request.data['email'])
        if not EmailAddress.objects.get(email=self.request.data['email']).verified:
            return Response('Email address is not confirmed', status=status.HTTP_403_FORBIDDEN)
        if not user.is_active:
            return Response('User is not active', status=status.HTTP_403_FORBIDDEN)
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()

class UserActionsView(LoggingMixin,generics.ListAPIView):
    """
    get:
    Return actions

    ---
        parameters:
        - name: action_type
        required: true
          type: str
    """
    serializer_class = UserActionSerializer
    queryset = UserAction.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ('action_type')
    ordering_fields = ('updated')
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class UserActionView(LoggingMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    patch:
    Update UserAction

    ---
        parameters:

        - action : action_type
          required: true
          type: int

    get:
    Return user

    ---
        parameters:

        - name: id
          action : action_type
          required: true
          type: int

    put:
    Update user

    ---
        parameters:

        - name: id
          action : action_type
          required: true
          type: int

    delete:
    Delete user

    ---
        parameters:

        - name: id
          action : action_type
          required: true
          type: int
    """
    permission_classes = [IsAdminUser]
    serializer_class = UserActionSerializer
    queryset = UserAction.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ('user','action_type')
    ordering_fields = ('updated')