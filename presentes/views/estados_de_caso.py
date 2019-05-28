from rest_framework import viewsets

from presentes.models.estados_de_caso import EstadoDeCaso
from presentes.serializers.estados_de_caso import EstadoDeCasoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class EstadoDeCasoViewSet(viewsets.ModelViewSet):
    queryset = EstadoDeCaso.objects.all()
    resource_name = 'estados_de_caso'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = EstadoDeCasoSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
