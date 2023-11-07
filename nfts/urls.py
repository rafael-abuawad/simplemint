from django.urls import path

from nfts.views import NFTFormView, NFTListView

urlpatterns = [
    path("", NFTListView.as_view(), name="nft-list"),
    path("mint/", NFTFormView.as_view(), name="nft-form"),
]
