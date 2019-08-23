from django.contrib import admin
from presentes.models.instituciones import Institucion


class InstitucionAdmin(admin.ModelAdmin):
    model = Institucion
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
