from django.contrib import admin
from django.contrib.auth.models import Permission
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from presentes.admin_classes.perfiles import Perfil, PerfilAdmin
from presentes.admin_classes.paises import Pais, PaisAdmin
from presentes.admin_classes.provincias import Provincia, ProvinciaAdmin
from presentes.admin_classes.categorias import Categoria, CategoriaAdmin
from presentes.admin_classes.organizaciones import Organizacion, OrganizacionAdmin
from presentes.admin_classes.etiquetas import Etiqueta, EtiquetaAdmin
from presentes.admin_classes.casos import Caso, CasoAdmin
from presentes.admin_classes.estados_de_caso import EstadoDeCaso, EstadoDeCasoAdmin

class MyGroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    permissions = forms.ModelMultipleChoiceField(
        Permission.objects.exclude(name__startswith='Can'),
        widget=admin.widgets.FilteredSelectMultiple('permissions', False))


class MyGroupAdmin(admin.ModelAdmin):
    form = MyGroupAdminForm
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Perfil, PerfilAdmin)
admin.site.unregister(Group)
admin.site.register(Group, MyGroupAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Caso, CasoAdmin)
admin.site.register(EstadoDeCaso, EstadoDeCasoAdmin)
