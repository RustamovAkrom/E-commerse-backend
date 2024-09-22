# Generated by Django 5.1.1 on 2024-09-21 16:54

import django.db.models.deletion
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSpecification",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required", max_length=255, verbose_name="Name"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification",
                "verbose_name_plural": "Product Specifications",
            },
        ),
        migrations.CreateModel(
            name="ProductType",
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
                (
                    "name",
                    models.CharField(
                        help_text="Required",
                        max_length=255,
                        unique=True,
                        verbose_name="Product Name",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="author",
        ),
        migrations.RemoveField(
            model_name="product",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.RemoveField(
            model_name="product",
            name="is_stock",
        ),
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
        migrations.AddField(
            model_name="category",
            name="level",
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="lft",
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="shop.category",
            ),
        ),
        migrations.AddField(
            model_name="category",
            name="rght",
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="tree_id",
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="regular_price",
            field=models.DecimalField(
                decimal_places=2,
                default=1,
                error_messages={
                    "name": {
                        "max_length": "THe price must be bettween o and 99999999.99"
                    }
                },
                help_text="Maximum 99999999.99",
                max_digits=10,
                verbose_name="Regular price",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="users_wishlist",
            field=models.ManyToManyField(
                blank=True, related_name="user_wishlist", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, help_text="Not Required", verbose_name="description"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(
                help_text="Required", max_length=255, verbose_name="title"
            ),
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "slug",
                    models.CharField(max_length=255, unique=True, verbose_name="URL"),
                ),
                (
                    "image",
                    models.ImageField(
                        default="images/default.png", upload_to="images/"
                    ),
                ),
                ("alt_text", models.CharField(blank=True, max_length=255, null=True)),
                ("is_feature", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image",
                        to="shop.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Image",
                "verbose_name_plural": "Product Images",
            },
        ),
        migrations.CreateModel(
            name="ProductSpecificationValue",
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
                (
                    "value",
                    models.CharField(
                        help_text="Product specification value (maximum of 255 words).",
                        max_length=255,
                        verbose_name="value",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_specification_values",
                        to="shop.product",
                    ),
                ),
                (
                    "specification",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_specification_values",
                        to="shop.productspecification",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Specification Value",
                "verbose_name_plural": "Product Specification Values",
            },
        ),
        migrations.AddField(
            model_name="productspecification",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="shop.producttype"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="products",
                to="shop.producttype",
            ),
            preserve_default=False,
        ),
    ]
