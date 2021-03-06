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
from presentes.admin_classes.archivos import Archivo, ArchivoAdmin
from presentes.admin_classes.estudios import Estudio, EstudioAdmin
from presentes.admin_classes.lugares_del_hecho import LugarDelHecho, LugarDelHechoAdmin
from presentes.admin_classes.espacios_privados import EspacioPrivado, EspacioPrivadoAdmin
from presentes.admin_classes.mecanicas_del_hecho import MecanicaDelHecho, MecanicaDelHechoAdmin
from presentes.admin_classes.instituciones import Institucion, InstitucionAdmin

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
admin.site.register(Archivo, ArchivoAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(LugarDelHecho, LugarDelHechoAdmin)
admin.site.register(EspacioPrivado, EspacioPrivadoAdmin)
admin.site.register(MecanicaDelHecho, MecanicaDelHechoAdmin)
admin.site.register(Institucion, InstitucionAdmin)
