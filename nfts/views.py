from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from nfts.forms import NFTForm, TraitFormset
from nfts.models import NFT, Properties, Trait


class NFTListView(ListView):
    model = NFT


class NFTFormView(FormView, LoginRequiredMixin):
    form_class = NFTForm
    template_name = "nfts/nft_form.html"
    success_url = reverse_lazy("nft-list")

    def form_valid(self, form):
        trait_formset = TraitFormset(self.request.POST)

        if form.is_valid() and trait_formset.is_valid():
            creator = form.cleaned_data.get("creator")
            properties = Properties.objects.create(creator=creator)
            properties.save()

            for t in trait_formset.cleaned_data:
                if len(t) != 0:
                    trait = Trait.objects.create(
                        name=t.get("name"),
                        type=t.get("type"),
                        value=t.get("value"),
                        properties=properties,
                    )
                    trait.save()

            nft = NFT.objects.create(
                name=form.cleaned_data.get("name"),
                description=form.cleaned_data.get("description"),
                image=form.cleaned_data.get("image"),
                is_public=form.cleaned_data.get("is_public"),
                properties=properties,
                owner=self.request.user,
            )
            img = form.cleaned_data.get("image")
            nft.image_integrity = NFT.calculate_hash(img)
            nft.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["trait_formset"] = TraitFormset()
        return context
