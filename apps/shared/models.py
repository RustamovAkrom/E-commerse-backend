from django.utils.translation import gettext_lazy as _
from django.db import models  # noqa


class TimestempedAbstractModel(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"),
        auto_now=True
    )

    class Meta:
        abstract = True


class SlugstempedAbstractModel(models.Model):
    slug = models.CharField(
        verbose_name=_("URL"),
        max_length=255, 
        unique=True
    )

    class Meta:
        abstract = True
