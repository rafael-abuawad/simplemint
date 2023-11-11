from rest_framework import generics

from nfts.models import NFT
from nfts.api.serializers import NFTSerializer


class NFTListView(generics.ListAPIView):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer


class NFTDetailView(generics.RetrieveAPIView):
    queryset = NFT.objects.all()
    serializer_class = NFTSerializer
