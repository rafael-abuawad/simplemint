from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("_/admin/", admin.site.urls),
    path("_/api/v1/nfts/", include("nfts.api.urls")),
    path("auth/", include("accounts.urls")),
    path("", include("nfts.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
