from django.contrib import admin
from presentes.models.categorias import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ('id', 'nombre')
    search_fields = ('nombre', )
