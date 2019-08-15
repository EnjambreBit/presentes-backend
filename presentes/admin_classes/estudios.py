from django.contrib import admin
from presentes.models.estudios import Estudio


class EstudioAdmin(admin.ModelAdmin):
    model = Estudio
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
