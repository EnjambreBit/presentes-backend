from rest_framework import viewsets

from presentes.models.provincias import Provincia
from presentes.serializers.provincias import ProvinciaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    resource_name = 'provincias'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = ProvinciaSerializer
    search_fields = []
    filterset_fields = []

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('query', '')
        nombre = self.request.query_params.get('nombre', '')
        ordenamiento = self.request.query_params.get('ordenamiento', '')

        queryset = queryset.filter(nombre__icontains=query)

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        return queryset
