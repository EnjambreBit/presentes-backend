from rest_framework import serializers
from presentes.models.perfiles import Perfil
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)

class PerfilSerializer(serializers.ModelSerializer):

    grupos = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Perfil
        fields = (
            'id',
            'nombre',
            'apellido',
            'email',
            'usuario',
            'grupos'
        )

    class JSONAPIMeta:
        included_resources = ['grupos']
