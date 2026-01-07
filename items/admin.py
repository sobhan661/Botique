from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma

from .models import ItemVariant, Item


class ItemVariantInline(admin.TabularInline):
    model = ItemVariant
    extra = 0
    min_num = 1
    validate_min = True


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "category",
        "formatted_price",
        "is_active",
    ]
    list_filter = [
        "category",
        "is_active",
    ]
    search_fields = ("name",)
    inlines = [ItemVariantInline]

    @admin.display(description="Price (Toman)")
    def formatted_price(self, obj):
        return intcomma(obj.price_toman)
