from rest_framework import viewsets

from aplicacion.models.modelo import Modelo
from aplicacion.serializers.modelo import ModeloSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    resource_name = 'modelo_plural'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = ModeloSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
