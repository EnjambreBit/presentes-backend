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
    imagen_url = serializers.SerializerMethodField()

    def get_imagen_url(self, object):
        if object.imagen:
            request = self.context.get('request')
            return request.build_absolute_uri(object.imagen.url)
        else:
            return None

    class Meta:
        model = Perfil
        fields = (
            'id',
            'nombre',
            'apellido',
            'email',
            'usuario',
            'grupos',
            'imagen_url'
        )

    class JSONAPIMeta:
        included_resources = ['grupos']
