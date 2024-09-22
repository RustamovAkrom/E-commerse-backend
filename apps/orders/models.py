from django.conf import settings
from django.db import models
from apps.shared.models import TimestempedAbstractModel
from apps.shop.models import Product


class Order(TimestempedAbstractModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_users"
    )
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country_code = models.CharField(max_length=4, blank=True)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    order_key = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"Order {str(self.created_at)}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"order:{self.order}, product:{self.product}"
