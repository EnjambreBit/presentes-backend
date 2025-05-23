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
import base64
from django.core.files.base import ContentFile
import urllib

from presentes.models.provincias import Provincia
from presentes.models.estados_de_caso import EstadoDeCaso
from presentes.models.categorias import Categoria
from presentes.models.etiquetas import Etiqueta

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
        etiqueta = self.request.query_params.get('etiqueta', '')

        ordenamiento = self.request.query_params.get('ordenamiento', '')

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        if nombre:
            queryset = queryset.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre))

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if provincia:
            provinciaComoObjeto = Provincia.objects.get(nombre=provincia)
            queryset = queryset.filter(provincia__in=[provinciaComoObjeto.id])

        if estadoDePublicacion:
            estadoComoObjeto = EstadoDeCaso.objects.get(nombre=estadoDePublicacion)
            queryset = queryset.filter(estado_de_publicacion__in=[estadoComoObjeto.id])

        if categoria:
            categoriacomoobjeto = Categoria.objects.get(nombre=categoria)
            queryset = queryset.filter(categoria__in=[categoriacomoobjeto.id])

        if etiqueta:
            etiquetaComoObjeto = Etiqueta.objects.get(nombre=etiqueta)
            queryset = queryset.filter(etiquetas__in=[etiquetaComoObjeto.id])

        queryset = queryset.distinct()

        return queryset


    @action(detail=False, permission_classes=[permissions.IsAuthenticatedOrReadOnly], methods=['get'], url_path='obtener-filtros')
    def obtener_filtros_para_casos_publicos(self, request, *args, **kwargs):
        lista_de_provincias = Provincia.objects.values_list('nombre', flat=True)
        lista_de_categorias = Categoria.objects.values_list('nombre', flat=True)
        lista_de_etiquetas = Etiqueta.objects.values_list('nombre', flat=True)

        data = {
          "keys": [
            {
              "key": "nombre",
              "title": "Nombre"
            },
            {
              "key": "categoria",
              "title": "Categoría",
              "valores": lista_de_categorias
            },
            {
              "key": "etiqueta",
              "title": "Etiqueta",
              "valores": lista_de_etiquetas
            },
            {
              "key": "localidad",
              "title": "Localidad"
            },
            {
              "key": "provincia",
              "title": "Provincia",
              "valores": lista_de_provincias
            }
          ]
        }

        return Response(data)

    @action(detail=False, permission_classes=[permissions.IsAuthenticatedOrReadOnly], methods=['get'], url_path='obtener-casos')
    def obtener_casos(self, request, *args, **kwargs):
        casos = Caso.objects.all()

        categoria = self.request.query_params.get('categoria', None)
        anio = self.request.query_params.get('anio', None)

        if anio:
            casos = casos.filter(fecha_del_hecho__year=anio)

        if categoria:
            categoriacomoobjeto = Categoria.objects.get(nombre=categoria)
            casos = casos.filter(categoria__in=[categoriacomoobjeto.id])

        data = []
        for c in casos:
            datos = {}
            datos.update({"id": c.id})
            datos.update({"nombre": c.nombre})
            datos.update({"apellido": c.apellido})
            datos.update({"nombreCompleto": f"{c.nombre} {c.apellido}"})
            datos.update({"calle": c.calle})
            datos.update({"localidad": c.localidad})
            datos.update({"provincia": c.provincia.nombre})
            datos.update({"fechaDelHecho": c.fecha_del_hecho})
            datos.update({"latitud": c.latitud})
            datos.update({"longitud": c.longitud})
            datos.update({"categoria": c.categoria.nombre})
            datos.update({"coordenadas": f"[{c.latitud}, {c.longitud}]"})
            datos.update({"copete": c.copete})
            datos.update({"linkDeNota": c.link_de_nota})
            datos.update({"dondeVivia": c.donde_vivia})
            datos.update({"paisDeOrigen": c.pais_de_origen})
            datos.update({"causaDeLaMuerte": c.causa_de_la_muerte})
            datos.update({"edad": c.edad})
            datos.update({"lugarDeNacimiento": c.lugar_de_nacimiento})
            if c.imagen:
                imagen_url = request.build_absolute_uri(c.imagen.url)
            else:
                imagen_url = None
            datos.update({"imagen_url": imagen_url})

            data.append(datos)

        return Response(data)

    @action(detail=False, permission_classes=[permissions.IsAuthenticatedOrReadOnly], methods=['get'], url_path='obtener-casos-publicos')
    def obtener_casos_publicos(self, request, *args, **kwargs):
        queryset = self.queryset

        search = self.request.query_params.get('search', None)
        nombre = self.request.query_params.get('nombre', None)
        categoria = self.request.query_params.get('categoria', None)
        etiqueta = self.request.query_params.get('etiqueta', '')
        localidad = self.request.query_params.get('localidad', None)
        provincia = self.request.query_params.get('provincia', '')
        anio = self.request.query_params.get('anio', None)

        if search and search != "null":
            queryset = queryset.filter(Q(nombre__icontains=search) | Q(apellido__icontains=search))

        if nombre:
            queryset = queryset.filter(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre))

        if categoria:
            categoriacomoobjeto = Categoria.objects.get(nombre=categoria)
            queryset = queryset.filter(categoria__in=[categoriacomoobjeto.id])

        if localidad:
            queryset = queryset.filter(localidad__icontains=localidad)

        if provincia:
            provinciaComoObjeto = Provincia.objects.get(nombre=provincia)
            queryset = queryset.filter(provincia__in=[provinciaComoObjeto.id])

        if etiqueta:
            etiquetaComoObjeto = Etiqueta.objects.get(nombre=etiqueta)
            queryset = queryset.filter(etiquetas__in=[etiquetaComoObjeto.id])

        if anio:
            queryset = queryset.filter(fecha_del_hecho__year=anio)


        queryset = queryset.filter(estado_de_publicacion__nombre="Público")

        queryset = queryset.distinct()

        return Response({
          "meta": { "pagination": { "page": 1, "pages": 1, "count": queryset.count()}},
          "filas": [c.serializar_para_lista() for c in queryset]
        })

    @action(detail=False, permission_classes=[permissions.IsAuthenticatedOrReadOnly], methods=['get'], url_path='obtener-casos-publicos-para-mapa')
    def obtener_casos_publicos_para_mapa(self, request, *args, **kwargs):
        self.pagination_class = None

        casos = Caso.objects.filter(estado_de_publicacion__nombre="Público")

        categoria = self.request.query_params.get('categoria', None)
        anio = self.request.query_params.get('anio', None)

        if anio:
            casos = casos.filter(fecha_del_hecho__year=anio)

        if categoria:
            categoriacomoobjeto = Categoria.objects.get(nombre=categoria)
            casos = casos.filter(categoria__in=[categoriacomoobjeto.id])

        return Response([c.serializar_para_mapa() for c in casos]
        )

    def create(self, request, *args, **kwargs):
        return super(CasoViewSet, self).create(request, *args, **kwargs)

    def perform_update(self, serializer):
        return self.guardar_modelo_con_archivo(serializer)

    def perform_create(self, serializer):
        return self.guardar_modelo_con_archivo(serializer)

    def guardar_modelo_con_archivo(self, serializer):
        instancia = serializer.save()
        imagen = self.request.data.get('imagen', None)

        if imagen and isinstance(imagen, dict):
            nombre = imagen.get('nombre')
            contenido = imagen.get('contenido')

            header, data = contenido.split(';base64,')
            decoded_file = base64.b64decode(data)
            content_file = ContentFile(decoded_file)
            instancia.imagen.save(nombre, content_file, save=False)

        instancia.save()
        return instancia
