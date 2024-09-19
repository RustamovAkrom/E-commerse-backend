from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")

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
