from django.contrib import admin
from presentes.models.provincias import Provincia


class ProvinciaAdmin(admin.ModelAdmin):
    model = Provincia
    list_display = ('id', 'nombre', 'sigla', 'pais')
    search_fields = ('nombre', )
