from django.contrib import admin
from presentes.admin_classes.perfiles import Perfil, PerfilAdmin

admin.site.register(Perfil, PerfilAdmin)
