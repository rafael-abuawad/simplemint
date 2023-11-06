from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("_/api/v1/auth/", include("accounts.api.urls")),
]
