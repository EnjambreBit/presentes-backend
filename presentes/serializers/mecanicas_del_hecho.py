from rest_framework import serializers
from presentes.models.mecanicas_del_hecho import MecanicaDelHecho

class MecanicaDelHechoSerializer(serializers.ModelSerializer):

    class Meta:
        model = MecanicaDelHecho
        fields = ('id', 'nombre')
