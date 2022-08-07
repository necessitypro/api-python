from rest_framework import serializers
from geography.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """serializer for country"""

    class Meta:
        model = Country
        fields = ("id", "name", "slug", "iso2", "iso3", "phone_code")
        read_only_fields = ("id", "slug")
