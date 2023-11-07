from django.urls import path, include

from accounts.views import UserCreationFormView

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", UserCreationFormView.as_view(), name="register"),
]
