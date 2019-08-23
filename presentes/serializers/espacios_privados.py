from rest_framework import serializers
from presentes.models.espacios_privados import EspacioPrivado


class EspacioPrivadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EspacioPrivado
        fields = ('id', 'nombre')
