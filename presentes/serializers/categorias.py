from rest_framework import serializers
from presentes.models.categorias import Categoria

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nombre')
