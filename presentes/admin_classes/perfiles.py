from django.contrib import admin
from presentes.models.perfiles import Perfil


class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
