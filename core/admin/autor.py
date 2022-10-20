from django.contrib import admin

from core.models import Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')
    list_filter = ('nome',)
    ordering = ('nome', 'email')

admin.site.register(Autor, AutorAdmin)