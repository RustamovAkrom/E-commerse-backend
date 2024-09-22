# Generated by Django 5.1.1 on 2024-09-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DeliveryOptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("delivery_name", models.CharField(max_length=255)),
                ("delivery_price", models.CharField(max_length=255)),
                (
                    "delivery_method",
                    models.CharField(
                        choices=[
                            ("is", "In Store"),
                            ("hd", "Home Delivery"),
                            ("dd", "Digital Delivery"),
                        ],
                        max_length=2,
                    ),
                ),
                ("delivery_timeframe", models.CharField(max_length=255)),
                ("delivery_window", models.CharField(max_length=255)),
                ("order", models.IntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Delivery Option",
                "verbose_name_plural": "Delivery Options",
            },
        ),
        migrations.CreateModel(
            name="PaymentSelections",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Payment Selection",
                "verbose_name_plural": "Payment Selections",
            },
        ),
    ]