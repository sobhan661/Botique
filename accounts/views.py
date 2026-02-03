from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser, Address
from .forms import CustomSignUpForm, AddressForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = Address.objects.filter(user=self.request.user).first()
        context["address_form"] = kwargs.get(
            "address_form",
            AddressForm(instance=address, prefix="address"),
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        address = Address.objects.filter(user=request.user).first()
        address_form = AddressForm(
            request.POST,
            instance=address,
            prefix="address",
        )

        if form.is_valid() and address_form.is_valid():
            return self.forms_valid(form, address_form)

        return self.forms_invalid(form, address_form)

    def forms_valid(self, form, address_form):
        response = super().form_valid(form)
        address = address_form.save(commit=False)
        address.user = self.request.user
        address.save()
        return response

    def forms_invalid(self, form, address_form):
        return self.render_to_response(
            self.get_context_data(form=form, address_form=address_form)
        )
