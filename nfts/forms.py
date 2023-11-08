from django import forms

from nfts.models import Trait


class NFTForm(forms.Form):
    name = forms.CharField(help_text="The name of the NFT")
    unit = forms.CharField(help_text="The symbol or unit of the NFT")
    total = forms.IntegerField()
    decimals = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    is_public = forms.BooleanField(required=False)
    creator = forms.CharField(required=False)
    mananger = forms.CharField(
        max_length=64,
        min_length=64,
        required=False,
        help_text="You can set the `mananger` field empty if you dont want the `mananger` functionality enabled.",
    )
    reserve = forms.CharField(
        max_length=64,
        min_length=64,
        required=False,
        help_text="You can set the `mananger` field empty if you dont want the `mananger` functionality enabled.",
    )
    freeze = forms.CharField(
        max_length=64,
        min_length=64,
        required=False,
        help_text="You can set the `freeze` field empty if you dont want the `freeze` functionality enabled.",
    )
    clawback = forms.CharField(
        max_length=64,
        min_length=64,
        required=False,
        help_text="You can set the `clawback` field empty if you dont want the `clawback` functionality enabled.",
    )


TraitFormset = forms.modelformset_factory(
    Trait, fields=("name", "value", "type"), extra=5
)
