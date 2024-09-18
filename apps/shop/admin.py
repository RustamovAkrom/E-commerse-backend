from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'price',
        'is_stock',
        'is_active',
        'created_at',
        'updated_at',
    ]
    list_filter = ['is_stock', 'is_active']
    list_editable = ['price', 'is_stock']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


