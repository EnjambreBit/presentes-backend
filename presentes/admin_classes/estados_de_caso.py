from django.contrib import admin
from presentes.models.estados_de_caso import EstadoDeCaso


class EstadoDeCasoAdmin(admin.ModelAdmin):
    model = EstadoDeCaso
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
