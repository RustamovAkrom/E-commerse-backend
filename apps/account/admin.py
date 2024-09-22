from django.contrib import admin

from .models import Address, CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "is_active",
    ]
    list_filter = ["username", "first_name", "last_name", "email", "phone_number"]
    search_fields = ["username", "first_name", "last_name", "email", "phone_number"]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "avatar",
        "user",
        "bio",
        "date_of_birth",
    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
