from django.contrib import admin
from presentes.admin_classes.perfiles import Perfil, PerfilAdmin
from presentes.admin_classes.paises import Pais, PaisAdmin
from presentes.admin_classes.provincias import Provincia, ProvinciaAdmin
from presentes.admin_classes.categorias import Categoria, CategoriaAdmin
from presentes.admin_classes.organizaciones import Organizacion, OrganizacionAdmin
from presentes.admin_classes.etiquetas import Etiqueta, EtiquetaAdmin

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Organizacion, OrganizacionAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
