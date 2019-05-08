from django.contrib import admin
from presentes.models.organizaciones import Organizacion


class OrganizacionAdmin(admin.ModelAdmin):
    model = Organizacion
    list_display = ('id', 'nombre', 'direccion', 'telefono', 'provincia')
    search_fields = ('nombre', )
