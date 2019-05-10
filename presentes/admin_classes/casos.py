from django.contrib import admin
from presentes.models.casos import Caso


class CasoAdmin(admin.ModelAdmin):
    model = Caso
    list_display = ('id', 'nombre', 'apellido', 'localidad', 'provincia', 'latitud', 'longitud', 'categoria', 'fecha_de_creacion')
    search_fields = ('nombre', 'apellido', 'localidad')
