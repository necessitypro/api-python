from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from geography.serializers import CountrySerializer
from geography.models import Country


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows countries to be viewed or edited.
    """

    queryset = Country.objects.filter(archived=False).order_by("name")
    serializer_class = CountrySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
