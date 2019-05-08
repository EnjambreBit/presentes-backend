from rest_framework import viewsets

from presentes.models.paises import Pais
from presentes.serializers.paises import PaisSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    resource_name = 'paises'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = PaisSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
