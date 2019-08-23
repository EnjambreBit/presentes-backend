from django.contrib import admin
from presentes.models.lugares_del_hecho import LugarDelHecho


class LugarDelHechoAdmin(admin.ModelAdmin):
    model = LugarDelHecho
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
