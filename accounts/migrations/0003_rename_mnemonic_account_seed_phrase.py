# Generated by Django 4.2.7 on 2023-11-08 01:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_account"),
    ]

    operations = [
        migrations.RenameField(
            model_name="account",
            old_name="mnemonic",
            new_name="seed_phrase",
        ),
    ]