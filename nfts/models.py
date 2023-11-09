from django.db import models
import hashlib

from accounts.models import User


class Properties(models.Model):
    creator = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Property (From {self.creator})"


class Trait(models.Model):
    class Types(models.Choices):
        STRING = "s"
        NUMBER = "n"

    name = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    type = models.CharField(max_length=64, choices=Types.choices, default=Types.STRING)
    properties = models.ForeignKey(
        Properties, on_delete=models.CASCADE, related_name="traits"
    )


class NFT(models.Model):
    name = models.CharField(max_length=256)
    unit = models.CharField(max_length=64)
    mananger = models.CharField(max_length=64, blank=True, default="")
    reserve = models.CharField(max_length=64, blank=True, default="")
    freeze = models.CharField(max_length=64, blank=True, default="")
    clawback = models.CharField(max_length=64, blank=True, default="")
    decimals = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="nfts/images")
    image_integrity = models.CharField(blank=True, max_length=64, editable=False)
    properties = models.OneToOneField(Properties, on_delete=models.CASCADE)
    index = models.IntegerField(blank=True, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
