from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from geography.models import Country
from geography.serializers import CountrySerializer


@pytest.mark.django_db
def test_list_countries():
    """test list countries"""
    client = APIClient()
    url = reverse("country-list")
    response = client.get(url)

    countries = Country.objects.filter(archived=False).order_by("name")
    expected_data = CountrySerializer(countries, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_country():
    """test create country"""
    client = APIClient()
    url = reverse("country-list")
    data = {
        "name": "United Kingdom",
        "iso2": "GB",
        "iso3": "GBR",
        "phone_code": 44,
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["name"] == "United Kingdom"
    assert response.data["slug"] == "united-kingdom"
    assert response.data["iso2"] == "GB"
    assert response.data["iso3"] == "GBR"
    assert response.data["phone_code"] == 44


@pytest.mark.django_db
def test_update_country():
    """test update country"""
    client = APIClient()
    url = reverse("country-list")
    data = {
        "name": "United Kingdom",
        "iso2": "GB",
        "iso3": "GBR",
        "phone_code": 44,
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["name"] == "United Kingdom"
    assert response.data["slug"] == "united-kingdom"
    assert response.data["iso2"] == "GB"
    assert response.data["iso3"] == "GBR"
    assert response.data["phone_code"] == 44

    updated_data = {
        "name": "United States of America",
        "iso2": "US",
        "iso3": "USA",
        "phone_code": 1,
    }

    url = reverse("country-detail", kwargs={"pk": response.data["id"]})
    response = client.put(url, updated_data)

    assert response.status_code == 200
    assert response.data["name"] == "United States of America"
    assert response.data["slug"] == "united-states-of-america"
    assert response.data["iso2"] == "US"
    assert response.data["iso3"] == "USA"
    assert response.data["phone_code"] == 1


@pytest.mark.django_db
def test_delete_country(client):
    """test delete country"""
    client = APIClient()
    url = reverse("country-list")
    data = {
        "name": "United Kingdom",
        "iso2": "GB",
        "iso3": "GBR",
        "phone_code": 44,
    }
    response = client.post(url, data)

    assert response.status_code == 201
    assert response.data["name"] == "United Kingdom"
    assert response.data["slug"] == "united-kingdom"
    assert response.data["iso2"] == "GB"
    assert response.data["iso3"] == "GBR"
    assert response.data["phone_code"] == 44

    id = response.data["id"]

    url = reverse("country-detail", kwargs={"pk": response.data["id"]})
    response = client.delete(url)

    assert response.status_code == 204
    country = Country.objects.get(id=id)
    assert country.archived is True
