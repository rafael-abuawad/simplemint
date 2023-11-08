from django.db.models.signals import post_save
from django.dispatch import receiver
from algosdk import account, mnemonic

from accounts.models import User, Account


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        private_key, address = account.generate_account()
        seed_phrase = mnemonic.from_private_key(private_key)
        Account.objects.create(
            address=address,
            seed_phrase=seed_phrase,
            private_key=private_key,
            owner=instance,
        )
