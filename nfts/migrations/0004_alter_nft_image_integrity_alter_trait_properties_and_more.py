# Generated by Django 4.2.7 on 2023-11-07 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("nfts", "0003_rename_properties_trait_properties_alter_nft_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nft",
            name="image_integrity",
            field=models.CharField(blank=True, editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name="trait",
            name="properties",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="traits",
                to="nfts.properties",
            ),
        ),
        migrations.AlterField(
            model_name="trait",
            name="type",
            field=models.CharField(
                choices=[("s", "String"), ("n", "Number")], default="s", max_length=64
            ),
        ),
    ]