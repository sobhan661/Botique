from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .models import CustomUser
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")
