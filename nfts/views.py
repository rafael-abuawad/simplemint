from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from nfts.forms import NFTForm
from nfts.models import NFT, Properties
from nfts.asa import asset_create


class NFTListView(ListView):
    model = NFT


class UserNFTListView(LoginRequiredMixin, ListView):
    model = NFT

    def get_queryset(self):
        return NFT.objects.filter(creator=self.request.user)


class NFTDetailView(DetailView):
    model = NFT


class NFTFormView(LoginRequiredMixin, FormView):
    form_class = NFTForm
    template_name = "nfts/nft_form.html"
    success_url = reverse_lazy("nft-list")

    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        initial["mananger"] = self.request.user.account.address
        initial["reserve"] = self.request.user.account.address
        initial["freeze"] = self.request.user.account.address
        initial["clawback"] = self.request.user.account.address
        return initial

    def form_valid(self, form):
        if form.is_valid():
            creator = self.request.user.account.address
            traits = (form.cleaned_data.get("traits"),)
            properties = Properties.objects.create(creator=creator, traits=traits)
            properties.save()

            nft = NFT.objects.create(
                name=form.cleaned_data.get("name"),
                unit=form.cleaned_data.get("unit"),
                manager=form.cleaned_data.get("manager"),
                reserve=form.cleaned_data.get("reserve"),
                freeze=form.cleaned_data.get("freeze"),
                clawback=form.cleaned_data.get("clawback"),
                description=form.cleaned_data.get("description"),
                image=form.cleaned_data.get("image"),
                properties=properties,
                creator=self.request.user,
            )

            url = f"/_/api/v1/nfts/{nft.pk}"
            i = asset_create(nft, url)

            img = form.cleaned_data.get("image")
            nft.image_integrity = NFT.calculate_hash(img)
            nft.index = i
            nft.save()

        return super(NFTFormView, self).form_valid(form)
