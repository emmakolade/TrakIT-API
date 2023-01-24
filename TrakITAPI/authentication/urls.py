
from .views import RegisterView, VerifyEmail, LoginView, PasswordTokenCheckAPIView, PasswordResetEmail, SetNewPassword
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
    path('request-reset/', PasswordResetEmail.as_view(), name='request-reset'),
    path('password-reset/<uidb64>/token/',
         PasswordTokenCheckAPIView.as_view(), name='password-reset'),
    path('password-reset-complete', SetNewPassword.as_view(),
         name='password-reset-complete'),
]
