
from .views import RegisterView, VerifyEmail, LoginView
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', VerifyEmail.as_view(), name='verify-email'),
]
