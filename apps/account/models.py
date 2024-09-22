import uuid

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.shared.models import TimestempedAbstractModel


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")

    @staticmethod
    def get_customuser_by_email(email):
        try:
            return CustomUser.objects.get(email=email)
        except Exception:
            return False

    def __str__(self) -> str:
        return self.username


class UserProfile(models.Model):
    GENDER_CHOICE = [
        ("male", "Male"),
        ("female", "Female"),
    ]

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, blank=True)

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self) -> str:
        return f"{self.user.username}`s Profile"


class Address(TimestempedAbstractModel):
    """
    Address.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        CustomUser, verbose_name=_("User"), on_delete=models.CASCADE
    )
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField("Town/City/State", max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)

    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return f"Address: {self.id}"
