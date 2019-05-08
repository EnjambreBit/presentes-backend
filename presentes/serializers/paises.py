from rest_framework import serializers
from presentes.models.paises import Pais


class PaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'sigla')
