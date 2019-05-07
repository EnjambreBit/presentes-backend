from django.contrib import admin
from presentes.models.perfiles import Perfil, PerfilAdmin

admin.site.register(Perfil, PerfilAdmin)
