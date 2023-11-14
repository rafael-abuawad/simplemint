from django.urls import path

from nfts.views import (
    NFTFormView,
    NFTListView,
    UserNFTListView,
    NFTDetailView,
    AboutView
)

urlpatterns = [
    path("", NFTListView.as_view(), name="nft-list"),
    path("nfts/", UserNFTListView.as_view(), name="user-nft-list"),
    path("nfts/mint/", NFTFormView.as_view(), name="nft-mint"),
    path("nfts/<int:pk>/", NFTDetailView.as_view(), name="nft-detail"),
    path("about/", AboutView.as_view(), name="about"),
]
