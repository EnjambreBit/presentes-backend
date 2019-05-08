from rest_framework import serializers
from presentes.models.etiquetas import Etiqueta


class EtiquetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Etiqueta
        fields = ('id', 'nombre')
