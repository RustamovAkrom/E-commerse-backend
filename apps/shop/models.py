from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from apps.shared.models import SlugstempedAbstractModel, TimestempedAbstractModel
from mptt.models import MPTTModel, TreeForeignKey
from .managers import ProductManager, CategoryManager


class Category(MPTTModel, TimestempedAbstractModel, SlugstempedAbstractModel):
    """
    Category Table implimented width MPTT.
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    # Managers
    objects = models.Manager()
    categories = CategoryManager()

    class MPTTMeta:
        order_insertion_by = "name"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self) -> str:
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types
    of products that are for sale.
    """

    name = models.CharField(
        verbose_name=_("Product Name"),
        help_text=_("Required"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self) -> str:
        return self.name


class ProductSpecification(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(
        verbose_name=_("Name"), help_text=_("Required"), max_length=255
    )

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(TimestempedAbstractModel, SlugstempedAbstractModel):
    """
    The Product table contining all product items.
    """

    product_type = models.ForeignKey(
        ProductType, on_delete=models.RESTRICT, related_name="products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    title = models.CharField(
        verbose_name=_("title"), help_text=_("Required"), max_length=255
    )
    description = models.TextField(
        verbose_name=_("description"), help_text=_("Not Required"), blank=True
    )
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 99999999.99"),
        error_messages={
            "name": {"max_length": _("THe price must be bettween o and 99999999.99")},
        },
        max_digits=10,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Miximum 99999999.99"),
        error_messages={
            "name": {"max_length": _("The price must be between 0 and 99999999.99")},
        },
        max_digits=10,
        decimal_places=2,
    )
    is_active = models.BooleanField(default=True)
    users_wishlist = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True
    )

    # Managers
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        return Product.get_all_products()

    def __str__(self) -> str:
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_specification_values"
    )
    specification = models.ForeignKey(
        ProductSpecification,
        on_delete=models.CASCADE,
        related_name="product_specification_values",
    )
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words)."),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(TimestempedAbstractModel, SlugstempedAbstractModel):
    """
    THe Product Image Table.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(upload_to="images/", default="images/default.png")
    alt_text = models.CharField(max_length=255, blank=True, null=True)
    is_feature = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")

    def __str__(self) -> str:
        return self.image.url


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
