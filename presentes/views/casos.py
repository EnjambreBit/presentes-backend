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

from presentes.models.provincias import Provincia
from presentes.models.estados_de_caso import EstadoDeCaso
from presentes.models.categorias import Categoria

class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    resource_name = 'casos'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = CasoSerializer
    search_fields = []
    filterset_fields = []

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('query', None)
        nombre = self.request.query_params.get('nombre', None)
        apellido = self.request.query_params.get('apellido', None)
        localidad = self.request.query_params.get('localidad', None)
        provincia = self.request.query_params.get('provincia', '')
        estadoDePublicacion = self.request.query_params.get('estadoDePublicacion', '')
        categoria = self.request.query_params.get('categoria', '')

        ordenamiento = self.request.query_params.get('ordenamiento', '')

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        if nombre:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if provincia:
            provinciaComoObjeto = Provincia.objects.get(nombre=provincia)
            queryset = queryset.filter(provincia__in=[provinciaComoObjeto.id])

        if estadoDePublicacion:
            estadoComoObjeto = EstadoDeCaso.objects.get(nombre=estadoDePublicacion)
            queryset = queryset.filter(estado_de_publicacion__in=[estadoComoObjeto.id])

        if categoria:
            categoriaComoObjeto = Categoria.objects.get(nombre=categoria)
            queryset = queryset.filter(categoria__in=[categoriaComoObjeto.id])

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
                "nombreCompleto": f"{c.nombre} {c.apellido}",
                "calle": c.calle,
                "localidad": c.localidad,
                "provincia": c.provincia.nombre,
                "fechaDelHecho": c.fecha_del_hecho,
                "latitud": c.latitud,
                "longitud": c.longitud,
                "categoria": c.categoria.nombre,
                "coordenadas": f"[{c.latitud}, {c.longitud}]",
                "copete": c.copete,
                "linkDeNota": c.link_de_nota,
                "dondeVivia": c.donde_vivia,
                "paisDeOrigen": c.pais_de_origen,
                "causaDeLaMuerte": c.causa_de_la_muerte,
                "edad": c.edad,
                "lugarDeNacimiento": c.lugar_de_nacimiento
            } for c in casos
        ]

        return Response(data)

    @action(detail=False, permission_classes=[permissions.IsAuthenticatedOrReadOnly], methods=['get'], url_path='obtener-casos-publicos')
    def obtener_casos_publicos(self, request, *args, **kwargs):
        casos = Caso.objects.filter(estado_de_publicacion__nombre="Público")

        data = [
            {
                "id": c.id,
                "nombre": c.nombre,
                "apellido": c.apellido,
                "nombreCompleto": f"{c.nombre} {c.apellido}",
                "calle": c.calle,
                "localidad": c.localidad,
                "provincia": c.provincia.nombre,
                "fechaDelHecho": c.fecha_del_hecho,
                "latitud": c.latitud,
                "longitud": c.longitud,
                "categoria": c.categoria.nombre,
                "coordenadas": f"[{c.latitud}, {c.longitud}]",
                "copete": c.copete,
                "linkDeNota": c.link_de_nota,
                "dondeVivia": c.donde_vivia,
                "paisDeOrigen": c.pais_de_origen,
                "causaDeLaMuerte": c.causa_de_la_muerte,
                "edad": c.edad,
                "lugarDeNacimiento": c.lugar_de_nacimiento
            } for c in casos
        ]

        return Response(data)

    def create(self, request, *args, **kwargs):
        return super(CasoViewSet, self).create(request, *args, **kwargs)
