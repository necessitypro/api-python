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


@pytest.mark.django_db
def test_delete_country():
    """test deleting a country"""
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

    country.delete()

    with pytest.raises(Country.DoesNotExist):
        Country.objects.get(id=country.id)


@pytest.mark.django_db
def test_get_country_by_id():
    """test getting a country by id"""
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

    country_by_id = Country.objects.get(id=country.id)

    assert country_by_id.id == country.id
    assert country_by_id.name == "United Kingdom"
    assert country_by_id.slug == slugify("United Kingdom")
    assert country_by_id.iso2 == "GB"
    assert country_by_id.iso3 == "GBR"
    assert country_by_id.phone_code == 44
    assert country_by_id.__str__() == "United Kingdom"


@pytest.mark.django_db
def test_get_all_countries():
    """test getting all countries"""
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

    country = Country.objects.create(
        name="United States of America",
        iso2="US",
        iso3="USA",
        phone_code=1,
    )

    assert country.id is not None
    assert country.name == "United States of America"
    assert country.slug == slugify("United States of America")
    assert country.iso2 == "US"
    assert country.iso3 == "USA"
    assert country.phone_code == 1
    assert country.__str__() == "United States of America"

    all_countries = Country.objects.all()

    assert all_countries.count() == 2

    assert all_countries[0].name == "United Kingdom"
    assert all_countries[0].slug == slugify("United Kingdom")
    assert all_countries[0].iso2 == "GB"
    assert all_countries[0].iso3 == "GBR"
    assert all_countries[0].phone_code == 44
    assert all_countries[0].__str__() == "United Kingdom"

    assert all_countries[1].name == "United States of America"
    assert all_countries[1].slug == slugify("United States of America")
    assert all_countries[1].iso2 == "US"
    assert all_countries[1].iso3 == "USA"
    assert all_countries[1].phone_code == 1
    assert all_countries[1].__str__() == "United States of America"
