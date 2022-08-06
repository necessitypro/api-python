"""default django packages"""
from django.db import models
from django.utils.text import slugify
from uuid import uuid4

from authentication.models import Account

"""
class AuditBaseModel(models.Model):
    

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(
        Account,
        on_delete=models.RESTRICT,
        related_name="%(class)s_created_by",
        editable=False,
    )
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    modified_by = models.ForeignKey(
        Account,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="%(class)s_modified_by",
        editable=False,
    )
    modified_diff = models.JSONField(null=True, blank=True, editable=False)
    archived = models.BooleanField(default=False)
    archived_on = models.DateTimeField(null=True, blank=True, editable=False)
    archived_by = models.ForeignKey(
        Account,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name="%(class)s_archived_by",
        editable=False,
    )
"""


class Country(models.Model):
    """country model"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="The name of the country")
    slug = models.SlugField(max_length=255, unique=True)
    iso2 = models.CharField(
        max_length=2, help_text="The ISO alpha-2 code of the country"
    )
    iso3 = models.CharField(
        max_length=3, help_text="The ISO alpha-3 code of the country"
    )
    phone_code = models.IntegerField(help_text="The phone code of the country")
    archived = models.BooleanField(default=False, help_text="Is the country archived?")

    class Meta:
        db_table = "geography_country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
