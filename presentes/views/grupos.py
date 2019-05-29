import json
from rest_framework import viewsets

from django.contrib.auth.models import Group, Permission
from presentes.serializers.grupos import GruposSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class GruposViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    resource_name = 'groups'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = GruposSerializer
    search_fields = ['name']
    filterset_fields = ['name']
    ordering = ('id',)

    def get_queryset(self):
        queryset = self.queryset
        nombre = self.request.query_params.get('nombre', '')
        ordenamiento = self.request.query_params.get('ordenamiento', '')

        if ordenamiento:
            queryset = queryset.order_by(ordenamiento)

        if nombre:
            queryset = queryset.filter(name__icontains=nombre)

        return queryset.order_by('name')

    @action(detail=False, methods=['post'], url_path='modificar-permisos')
    def modificar_permisos(self, request, *args, **kwargs):
        datos = json.loads(request.body)
        grupo_id = datos['grupo_id']
        codigo_permisos = datos['permisos']
        grupo = Group.objects.get(id=grupo_id)
        permisos = Permission.objects.filter(codename__in=codigo_permisos)
        grupo.permissions.set(permisos)
        return Response({ "ok": True })
