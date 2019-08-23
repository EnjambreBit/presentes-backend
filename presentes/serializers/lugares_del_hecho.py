from rest_framework import serializers
from presentes.models.lugares_del_hecho import LugarDelHecho


class LugarDelHechoSerializer(serializers.ModelSerializer):

    class Meta:
        model = LugarDelHecho
        fields = ('id', 'nombre')
