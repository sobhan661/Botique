from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number required")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = PhoneNumberField(
        "Phone Number",
        unique=True,
        region="IR",
    )
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=50)
    email = models.EmailField(
        "Email",
        unique=True,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    is_active = models.BooleanField("Active Status", default=True)
    is_staff = models.BooleanField("Staff Status", default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="address",
    )
    street_address = models.CharField("Street Address", max_length=255)
    city = models.CharField("City", max_length=100)
    state = models.CharField("State", max_length=100)
    postal_code = models.CharField("Postal Code", max_length=20)
    country = models.CharField("Country", max_length=100, default="Iran")
    updated_at = models.DateTimeField("Updated At", auto_now=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.city}"
