from rest_framework import serializers
from nfts.models import Properties, NFT


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = "__all__"


class NFTSerializer(serializers.ModelSerializer):
    properties = PropertiesSerializer()

    class Meta:
        model = NFT
        fields = "__all__"
