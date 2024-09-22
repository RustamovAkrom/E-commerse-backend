from django.db import models


class DeliveryChoices(models.TextChoices):
    IN_STORE = "is", "In Store"
    HOME_DELIVERY = "hd", "Home Delivery"
    DIGITAL_DELIVERY = "dd", "Digital Delivery"
