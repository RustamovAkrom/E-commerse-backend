from django.db import models
from django.utils.translation import gettext_lazy as _
from .choices import DeliveryChoices


class DeliveryOptions(models.Model):
    """
    The Delivery methods table contining all delivery
    """

    delivery_name = models.CharField(max_length=255)
    delivery_price = models.CharField(max_length=255)
    delivery_method = models.CharField(max_length=2, choices=DeliveryChoices.choices)
    delivery_timeframe = models.CharField(max_length=255)
    delivery_window = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Delivery Option")
        verbose_name_plural = _("Delivery Options")

    def __str__(self) -> str:
        return self.delivery_name


class PaymentSelections(models.Model):
    """
    Shop payment options
    """

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Payment Selection")
        verbose_name_plural = _("Payment Selections")

    def __str__(self):
        return self.name
