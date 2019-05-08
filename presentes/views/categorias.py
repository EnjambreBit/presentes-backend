from rest_framework import viewsets

from presentes.models.categorias import Categoria
from presentes.serializers.categorias import CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import permissions

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    resource_name = 'categorias'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = CategoriaSerializer
    search_fields = ['nombre']
    filterset_fields = ['nombre']
