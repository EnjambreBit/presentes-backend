from rest_framework import viewsets

from presentes.models.organizaciones import Organizacion
from presentes.serializers.organizaciones import OrganizacionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.all()
    resource_name = 'organizaciones'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = OrganizacionSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
