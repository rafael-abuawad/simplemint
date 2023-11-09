import hashlib
import uuid
from django.db import models

from accounts.models import User


class Properties(models.Model):
    creator = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    traits = models.JSONField(default=dict)

    def __str__(self) -> str:
        return f"Property (From {self.creator})"


class NFT(models.Model):
    name = models.CharField(max_length=256)
    unit = models.CharField(max_length=64)
    decimals = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    description = models.TextField()
    index = models.IntegerField(blank=True, default=0)
    is_claimable = models.BooleanField(default=False)
    claim_token = models.UUIDField(default="")

    # management
    manager = models.CharField(max_length=64, blank=True, null=True, default="")
    reserve = models.CharField(max_length=64, blank=True, null=True, default="")
    freeze = models.CharField(max_length=64, blank=True, null=True, default="")
    clawback = models.CharField(max_length=64, blank=True, null=True, default="")

    # image
    image = models.ImageField(upload_to="nfts/images")
    image_integrity = models.CharField(blank=True, max_length=64, editable=False)

    # relations
    properties = models.OneToOneField(Properties, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def generate_claim_token(self):
        self.is_claimable = True
        self.claim_token = uuid.uuid4()
    
    def claim_token(self):
        self.is_claimable = True
        self.claim_token = "" 
    
    @classmethod
    def calculate_hash(cls, image):
        sha256 = hashlib.sha256()
        with image.open("rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()

    def __str__(self) -> str:
        return self.name
