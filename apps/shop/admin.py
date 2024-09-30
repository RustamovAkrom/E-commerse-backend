from django.contrib import admin
from .models import (
    Product,
    Category,
    Contact,
    ProductImage,
    ProductType,
    ProductSpecification,
    ProductSpecificationValue,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "regular_price",
        "discount_price",
        "is_active",
    ]
    list_filter = ["title", "is_active"]
    search_fields = ["title", "description", "regular_price", "discount_price"]
    fields = [
        "title",
        "slug",
        "category",
        "product_type",
        "description",
        "regular_price",
        "discount_price",
        "is_active",
        "users_wishlist",
    ]
    list_editable = ["regular_price", "discount_price", "is_active"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ["name", "product_type"]


@admin.register(ProductSpecificationValue)
class ProductSpecificationValue(admin.ModelAdmin):
    list_display = ["product", "specification", "value"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "is_active"]
    fields = ["name", "slug", "is_active"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "subject",
        "message",
    ]
    list_filter = ["created_at"]
    search_fields = ["name", "email"]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["product", "image", "alt_text", "is_feature"]
