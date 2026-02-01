from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser
from .forms import CustomSignUpForm

# Authentication Views


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomSignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


# Profile Views


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    context_object_name = "user"
    template_name = "profile.html"

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = [
        "first_name",
        "last_name",
        "email",
    ]
    success_url = reverse_lazy("profile")
    template_name = "profile_update.html"

    def get_object(self):
        return self.request.user
