from django import forms


class NFTForm(forms.Form):
    name = forms.CharField(help_text="The name of the NFT")
    unit = forms.CharField(help_text="The symbol or unit of the NFT")
    total = forms.IntegerField()
    decimals = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()
    traits = forms.JSONField(
        required=False,
        help_text="You need to input valid JSON to make it work.",
    )
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
