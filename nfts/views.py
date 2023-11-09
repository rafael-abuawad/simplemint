from typing import Any, Dict
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from nfts.forms import NFTForm, TraitFormset
from nfts.models import NFT, Properties, Trait
from nfts.asa import asset_create


class NFTListView(ListView):
    model = NFT


class UserNFTListView(LoginRequiredMixin, ListView):
    model = NFT

    def get_queryset(self):
        return NFT.objects.filter(owner=self.request.user)


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
                unit=form.cleaned_data.get("unit"),
                mananger=form.cleaned_data("manager"),
                reserve=form.cleaned_data("reserve"),
                freeze=form.cleaned_data("freeze"),
                clawback=form.cleaned_data("clawback"),
                description=form.cleaned_data.get("description"),
                image=form.cleaned_data.get("image"),
                index=asset_create(self.request.user.account),
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


class NFTClaim(LoginRequiredMixin, TemplateView):
    template_name = "nfts/nft_claim.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["nft"] = NFT.objects.get(pk=1)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
