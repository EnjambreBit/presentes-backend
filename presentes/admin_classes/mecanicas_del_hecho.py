from django.contrib import admin
from presentes.models.mecanicas_del_hecho import MecanicaDelHecho


class MecanicaDelHechoAdmin(admin.ModelAdmin):
    model = MecanicaDelHecho
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
