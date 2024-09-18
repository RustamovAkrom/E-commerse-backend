from django.contrib import admin
from .models import CustomUser, UserProfile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'avatar',
        'is_active',
    ]
    list_filter = [
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'phone_number'
    ]
    search_fields = [        
        'username', 
        'first_name', 
        'last_name', 
        'email', 
        'phone_number'
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'bio',
        'date_of_berth',
        'website',
    ]