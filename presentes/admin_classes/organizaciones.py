from django.contrib import admin
from presentes.models.organizaciones import Organizacion


class OrganizacionAdmin(admin.ModelAdmin):
    model = Organizacion
    list_display = ('id', 'nombre', 'telefono', 'email', 'direccion', 'localidad', 'provincia')
    search_fields = ('nombre', )
