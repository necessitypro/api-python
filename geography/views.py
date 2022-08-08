from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from geography.serializers import CountrySerializer
from geography.models import Country


class CountryViewSet(viewsets.ModelViewSet):
    """country api endpoint model view set"""

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.DjangoObjectPermissions,)

    def get_queryset(self):
        """override get queryset"""
        user = self.request.user

        if user.is_superuser:
            return self.filter_queryset(self.queryset)

        return self.filter_queryset(self.queryset.filter(archived=False))

    def destroy(self, request, *args, **kwargs):
        """override destroy method to archive country"""
        instance = self.get_object()
        instance.archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
