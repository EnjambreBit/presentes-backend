from rest_framework import viewsets

from presentes.models.archivos import Archivo
from presentes.serializers.archivos import ArchivoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    resource_name = 'archivos'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = ArchivoSerializer
    search_fields = []
    filterset_fields = []
