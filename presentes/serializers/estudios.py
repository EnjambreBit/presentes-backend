from rest_framework import serializers
from presentes.models.estudios import Estudio

class EstudioSerializer(serializers.ModelSerializer):


    class Meta:
        model = Estudio
        fields = (
            'id',
            'nombre',
        )
