from django.urls import path
from django.shortcuts import redirect

from .views import HomeView

urlpatterns = [
    path("", lambda x: redirect("home")),
    path("home", HomeView.as_view(), name="home"),
]
