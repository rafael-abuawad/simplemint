from django.contrib import admin

from nfts.models import NFT, Properties, Trait

admin.site.register([NFT, Properties, Trait])
