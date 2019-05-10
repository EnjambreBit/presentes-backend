from rest_framework import viewsets
import json
from presentes.models.casos import Caso
from presentes.serializers.casos import CasoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from django.db import IntegrityError
from django.db.models import Q

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    resource_name = 'casos'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = CasoSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('query', None)
        nombre = self.request.query_params.get('nombre', None)
        apellido = self.request.query_params.get('apellido', None)
        localidad = self.request.query_params.get('apellido', None)

        ordenamiento = self.request.query_params.get('ordenamiento', '')

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)

        queryset = queryset.distinct()

        return queryset

    @action(detail=False, permission_classes=[permissions.AllowAny], methods=['get'], url_path='obtener-casos')
    def obtener_casos(self, request, *args, **kwargs):
        casos = Caso.objects.all()

        data = [
            {
                "id": c.id,
                "nombre": c.nombre,
                "apellido": c.apellido,
                "localidad": c.localidad,
                "provincia": c.provincia.nombre,
                "fecha": c.fecha_del_hecho,
                "latitud": c.latitud,
                "longitud": c.longitud,
                "categoria": c.categoria.nombre,
                "coordenadas": f"[{c.latitud}, {c.longitud}]"
            } for c in casos
        ]

        return Response(data)
