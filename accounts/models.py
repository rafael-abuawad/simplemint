from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Account(models.Model):
    address = models.CharField(max_length=64)
    private_key = models.CharField(max_length=64)
    seed_phrase = models.TextField()
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="account", primary_key=True
    )

    def __str__(self) -> str:
        return self.address
