from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Item


class ItemView(DetailView):
    model = Item
    context_object_name = "item"
    template_name = "item.html"


class ItemsView(ListView):
    model = Item
    context_object_name = "items"
    template_name = "items.html"
