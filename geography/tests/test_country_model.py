from django.utils.text import slugify
import pytest

from geography.models import Country


@pytest.mark.django_db
def test_create_country():
    """test creating a country"""

    country = Country.objects.create(
        name="United Kingdom",
        iso2="GB",
        iso3="GBR",
        phone_code=44,
    )

    assert country.id is not None
    assert country.name == "United Kingdom"
    assert country.slug == slugify("United Kingdom")
    assert country.iso2 == "GB"
    assert country.iso3 == "GBR"
    assert country.phone_code == 44
    assert country.__str__() == "United Kingdom"


@pytest.mark.django_db
def test_update_country():
    """test updating a country"""

    country = Country.objects.create(
        name="United Kingdom",
        iso2="GB",
        iso3="GBR",
        phone_code=44,
    )

    assert country.id is not None
    assert country.name == "United Kingdom"
    assert country.slug == slugify("United Kingdom")
    assert country.iso2 == "GB"
    assert country.iso3 == "GBR"
    assert country.phone_code == 44
    assert country.__str__() == "United Kingdom"

    updated_country = Country.objects.get(id=country.id)
    updated_country.name = "United States of America"
    updated_country.iso2 = "US"
    updated_country.iso3 = "USA"
    updated_country.phone_code = 1
    updated_country.save()

    assert updated_country.name == "United States of America"
    assert updated_country.slug == slugify("United States of America")
    assert updated_country.iso2 == "US"
    assert updated_country.iso3 == "USA"
    assert updated_country.phone_code == 1
    assert updated_country.__str__() == "United States of America"
