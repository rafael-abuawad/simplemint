from django.urls import path
from nfts.api.views import NFTListView, NFTDetailView


urlpatterns = [
    path("", NFTListView.as_view()),
    path("<int:pk>/", NFTDetailView.as_view()),
]
