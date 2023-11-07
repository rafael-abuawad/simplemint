from django.views.generic import FormView

from accounts.forms import UserCreationForm


class UserCreationFormView(FormView):
    form_class = UserCreationForm
    fields = "__all__"
    template_name = "registration/register.html"
