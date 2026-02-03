from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Address


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = [AddressInline]

    list_display = [
        "get_full_name",
        "phone_number",
        "is_active",
    ]

    search_fields = ("phone_number", "first_name", "last_name", "email")
    ordering = ("phone_number",)

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "password",
                    "phone_number",
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "created_at",
                )
            },
        ),
    )

    readonly_fields = (
        "last_login",
        "created_at",
        "phone_number",
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
