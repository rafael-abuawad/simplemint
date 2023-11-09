from django.contrib import admin

from nfts.models import NFT, Properties

admin.site.register([NFT, Properties])
