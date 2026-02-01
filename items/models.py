from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):

    class Category(models.TextChoices):
        SHOES = "shoes", "Shoes"
        PANTS = "pants", "Pants"
        SHIRT = "shirt", "Shirt"
        OTHER = "other", "Other"

    name = models.CharField("Name", max_length=255)

    category = models.CharField(
        "Category",
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
    )

    price_toman = models.PositiveBigIntegerField(
        "Price (Toman)",
        validators=[MinValueValidator(100_000)],
        help_text="Price is in toman",
    )

    item_img = models.ImageField(
        "Item Image", upload_to="media/", blank=False, null=False
    )

    description = models.TextField("Description", blank=True)

    created_at = models.DateTimeField("Creation Date", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    is_active = models.BooleanField("Item Available", default=True)

    def __str__(self):
        return self.name


class ItemVariant(models.Model):

    class Size(models.TextChoices):
        XS = "xs", "XS"
        S = "s", "S"
        M = "m", "M"
        L = "l", "L"
        XL = "xl", "XL"
        XXL = "xxl", "XXL"

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="variants",
    )

    size = models.CharField(
        max_length=5,
        choices=Size.choices,
    )

    stock = models.PositiveIntegerField(
        default=0,
        help_text="Stock for this specific size",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["item", "size"], name="unique_item_size")
        ]

    def __str__(self):
        return f"{self.item.name} - {self.get_size_display()}"
