# Generated by Django 4.2.7 on 2023-11-13 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Properties",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creator", models.CharField(max_length=64)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("traits", models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name="NFT",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("unit", models.CharField(max_length=64)),
                ("decimals", models.IntegerField(default=0)),
                ("total", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("index", models.IntegerField(blank=True, default=0)),
                ("is_claimable", models.BooleanField(default=False)),
                (
                    "manager",
                    models.CharField(blank=True, default="", max_length=64, null=True),
                ),
                (
                    "reserve",
                    models.CharField(blank=True, default="", max_length=64, null=True),
                ),
                (
                    "freeze",
                    models.CharField(blank=True, default="", max_length=64, null=True),
                ),
                (
                    "clawback",
                    models.CharField(blank=True, default="", max_length=64, null=True),
                ),
                ("image", models.ImageField(upload_to="nfts/images")),
                (
                    "image_integrity",
                    models.CharField(blank=True, editable=False, max_length=64),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "properties",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nfts.properties",
                    ),
                ),
            ],
        ),
    ]
