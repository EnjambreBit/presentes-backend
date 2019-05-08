from django.contrib import admin
from presentes.models.paises import Pais


class PaisAdmin(admin.ModelAdmin):
    model = Pais
    list_display = ('id', 'nombre', 'sigla')
    search_fields = ('nombre', )
