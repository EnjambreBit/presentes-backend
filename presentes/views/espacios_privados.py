from rest_framework import viewsets

from presentes.models.espacios_privados import EspacioPrivado
from presentes.serializers.espacios_privados import EspacioPrivadoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class EspacioPrivadoViewSet(viewsets.ModelViewSet):
    queryset = EspacioPrivado.objects.all()
    resource_name = 'espacios-privados'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = EspacioPrivadoSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
