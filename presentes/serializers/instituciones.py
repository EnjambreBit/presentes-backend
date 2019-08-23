from rest_framework import serializers
from presentes.models.instituciones import Institucion


class InstitucionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institucion
        fields = ('id', 'nombre')
