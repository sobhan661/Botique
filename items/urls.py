from django.urls import path

from .views import ItemView, ItemsView

urlpatterns = [
    path("<int:pk>/", ItemView.as_view(), name="item"),
    path("", ItemsView.as_view(), name="items"),
]
