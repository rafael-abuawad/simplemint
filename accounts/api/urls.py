from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("login/", views.UserTokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login-refresh"),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
    path("", views.get_routes),
]
