from django import forms

from nfts.models import Trait


class NFTForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    is_public = forms.BooleanField(required=False)
    creator = forms.CharField(required=False)


TraitFormset = forms.modelformset_factory(
    Trait, fields=("name", "value", "type"), extra=5
)
