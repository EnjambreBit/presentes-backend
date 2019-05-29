from rest_framework import serializers
from django.contrib.auth.models import Group

class GruposSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')
