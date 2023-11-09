from django.urls import path

from nfts.views import (
    NFTFormView,
    NFTListView,
    UserNFTListView,
    NFTDetailView,
    nft_claim,
)

urlpatterns = [
    path("", NFTListView.as_view(), name="nft-list"),
    path("nfts/", UserNFTListView.as_view(), name="user-nft-list"),
    path("nfts/mint/", NFTFormView.as_view(), name="nft-mint"),
    path("nfts/<int:pk>/", NFTDetailView.as_view(), name="nft-detail"),
    path("nfts/<int:pk>/claim/", nft_claim, name="nft-claim"),
]
