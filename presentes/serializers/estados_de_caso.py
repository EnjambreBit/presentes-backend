from rest_framework import serializers
from presentes.models.estados_de_caso import EstadoDeCaso


class EstadoDeCasoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoDeCaso
        fields = [
            'id',
            'nombre'
        ]

    class JSONAPIMeta:
        included_resources = [
        ]
