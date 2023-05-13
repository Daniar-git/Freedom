from django.urls import path
from dj_rest_auth.views import PasswordResetConfirmView
from allauth.account.views import confirm_email as allauthemailconfirmation

from . import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('login/', views.CustomLoginView.as_view()),
    path('user/all/', views.UsersView.as_view()),
    path('user/detail/<int:pk>/', views.UserDetailView.as_view()),
    path('user/create/', views.CreateSuperuserView.as_view()),
    path('password/reset/', views.PasswordReset.as_view()),
    path('google/login/', views.GoogleLogin.as_view()),
    path('facebook/login/', views.FacebookLogin.as_view()),
    path('password/reset/confrim/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('registration/account-confirm-email/<key>/',
         allauthemailconfirmation,
         name='account_confirm_email'),
    path('user/action/', views.UserActionsView.as_view()),
    path('user/action/<int:pk>/', views.UserActionView.as_view())
]
