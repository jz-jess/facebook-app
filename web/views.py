from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class LoginView(TemplateView):
    template_name = 'login.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
