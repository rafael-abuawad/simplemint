from django.urls import path

from nfts.views import NFTFormView, NFTListView, NFTDetailView, NFTClaim

urlpatterns = [
    path("", NFTListView.as_view(), name="nft-list"),
    path("<int:pk>/", NFTDetailView.as_view(), name="nft-detail"),
    path("<intpk>/claim/", NFTClaim.as_view(), name="nft-claim"),
    path("mint/", NFTFormView.as_view(), name="nft-form"),
]
