from rest_framework import viewsets, status
from rest_framework.response import Response

from geography.serializers import CountrySerializer
from geography.models import Country


class CountryViewSet(viewsets.ModelViewSet):
    """country api endpoint model view set"""

    queryset = Country.objects.filter(archived=False).order_by("name")
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        """override destroy method to archive country"""
        instance = self.get_object()
        instance.archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
