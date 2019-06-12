from rest_framework import viewsets

from presentes.models.organizaciones import Organizacion
from presentes.serializers.organizaciones import OrganizacionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

from presentes.models.provincias import Provincia

class OrganizacionViewSet(viewsets.ModelViewSet):
    queryset = Organizacion.objects.all()
    resource_name = 'organizaciones'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = OrganizacionSerializer
    search_fields = []
    filterset_fields = []

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('query', '')
        nombre = self.request.query_params.get('nombre', '')
        localidad = self.request.query_params.get('localidad', None)
        provincia = self.request.query_params.get('provincia', '')
        ordenamiento = self.request.query_params.get('ordenamiento', '')

        queryset = queryset.filter(nombre__icontains=query)

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if provincia:
            provinciaComoObjeto = Provincia.objects.get(nombre=provincia)
            queryset = queryset.filter(provincia__in=[provinciaComoObjeto.id])

        return queryset
