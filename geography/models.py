"""default django packages"""
from django.db import models
from django.utils.text import slugify

from uuid import uuid4


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
        """meta class"""

        db_table = "geography_country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """override save method to set slug"""
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
