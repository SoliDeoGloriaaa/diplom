from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    """После успешной регистрации пользователь попадает на главную страницу."""
    form_class = CreationForm
    success_url = reverse_lazy('main:index')
    template_name = 'users/register.html'
