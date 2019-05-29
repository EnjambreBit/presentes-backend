from rest_framework import viewsets
import json
from presentes.models.perfiles import Perfil
from presentes.serializers.perfiles import PerfilSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from django.db import IntegrityError
from django.contrib.auth.models import Group, User
from backend.settings import BACKEND_URL, VERSION_NUMBER
from django.db.models import Q

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    resource_name = 'perfiles'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = PerfilSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']

    def get_queryset(self):
        queryset = self.queryset
        query = self.request.query_params.get('query', None)
        usuario = self.request.query_params.get('usuario', '')
        nombre = self.request.query_params.get('nombre', None)
        apellido = self.request.query_params.get('apellido', None)
        email = self.request.query_params.get('email', None)
        ordenamiento = self.request.query_params.get('ordenamiento', '')

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if query:
            queryset = queryset.filter(Q(nombre__icontains=query) | Q(apellido__icontains=query))

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)

        if email:
            queryset = queryset.filter(user__email__icontains=email)

        queryset = queryset.distinct()

        return queryset

    @action(detail=False, methods=['get'], url_path='mi-perfil')
    def mi_perfil(self, request, *args, **kwargs):
        perfil = Perfil.objects.get(user=request.user)

        data = {
            'id': perfil.id,
            'nombre': perfil.nombre,
            'apellido': perfil.apellido,
            'email': perfil.email(),
            'usuario': perfil.user.username,
            'version_del_servidor': VERSION_NUMBER,
            'permisos': perfil.obtener_diccionario_de_permisos(),
        }

        return Response(data)

    @action(detail=False, methods=['get'], url_path='obtener-nombres')
    def obtener_nombres(self, request, *args, **kwargs):
        perfiles = Perfil.objects.all()

        data = [
            {
                "key": f"{p.nombre} {p.apellido}",
                "value": p.user.username
            } for p in perfiles
        ]

        return Response(data)
