from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models  # noqa
from apps.shared.models import SlugstempedAbstractModel, TimestempedAbstractModel
from .managers import ProductManager, CategoryManager


class Category(TimestempedAbstractModel, SlugstempedAbstractModel):
    """
    Category Table.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    # Managers
    objects = models.Manager()
    categories = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name


class Product(TimestempedAbstractModel, SlugstempedAbstractModel):
    """
    Product Table.
    """

    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product_creator",
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", default="images/default.png")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    # Managers
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title


class Contact(TimestempedAbstractModel):
    """
    Contact Table.
    """
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.name
