from django.contrib import admin

from core.models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)

admin.site.register(Categoria, CategoriaAdmin)