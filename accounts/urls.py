from django.urls import path

from .views import (
    SignUpView,
    CustomLoginView,
    CustomLogoutView,
    ProfileView,
    ProfileUpdateView,
)

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", CustomLoginView.as_view(), name="login"),
    path("logout", CustomLogoutView.as_view(), name="logout"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update"),
]
