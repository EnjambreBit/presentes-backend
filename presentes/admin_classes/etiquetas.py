from django.contrib import admin
from presentes.models.etiquetas import Etiqueta


class EtiquetaAdmin(admin.ModelAdmin):
    model = Etiqueta
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
