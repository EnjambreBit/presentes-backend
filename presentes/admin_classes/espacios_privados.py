from django.contrib import admin
from presentes.models.espacios_privados import EspacioPrivado


class EspacioPrivadoAdmin(admin.ModelAdmin):
    model = EspacioPrivado
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
