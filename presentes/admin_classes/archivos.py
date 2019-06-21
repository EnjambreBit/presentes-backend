from django.contrib import admin
from presentes.models.archivos import Archivo


class ArchivoAdmin(admin.ModelAdmin):
    model = Archivo
    list_display = ('id', 'archivo', 'caso')
    search_fields = ('caso__nombre', )
