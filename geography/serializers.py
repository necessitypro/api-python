from rest_framework import serializers

from geography.models import Country


class CountrySerializer(serializers.ModelSerializer):
    """serializer for country"""

    class Meta:
        """meta class"""

        model = Country
        fields = ("id", "name", "slug", "iso2", "iso3", "phone_code", "archived")
        read_only_fields = ("id", "slug", "archived")
