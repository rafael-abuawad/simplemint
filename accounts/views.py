from django.views.generic import FormView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from accounts.forms import UserCreationForm


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = "registration/password-change.html"


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "registration/password-change-done.html"


class PasswordResetView(auth_views.PasswordResetView):
    template_name = "registration/password-reset.html"


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "registration/password-reset-done.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "registration/password-reset-confirm.html"


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "registration/password-reset-complete.html"


class UserCreationFormView(FormView):
    form_class = UserCreationForm
    fields = "__all__"
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
