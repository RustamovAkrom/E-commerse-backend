from django.db import models  # noqa


class TimestempedAbstractModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugstempedAbstractModel(models.Model):
    slug = models.CharField(max_length=200)

    class Meta:
        abstract = True
