from django.db import models

from accounts.models import User


class Properties(models.Model):
    creator = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    traits = models.JSONField()

    def __str__(self) -> str:
        return f"Property (From {self.creator})"


class NFT(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    image = models.URLField()
    image_integrity = models.CharField(max_length=256)
    is_public = models.BooleanField(blank=False, default=False)
    properties = models.OneToOneField(Properties, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
