from django.urls import path
from drf_spectacular.utils import extend_schema
from drf_spectacular.openapi import AutoSchema
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView


class DecoratedTokenObtainPairView(TokenObtainPairView):
    schema = AutoSchema()


class DecoratedTokenRefreshView(TokenRefreshView):
    schema = AutoSchema()


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
]