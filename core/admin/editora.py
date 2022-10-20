from django.contrib import admin

from core.models import Editora

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    list_filter = ('nome',)
    ordering = ('nome',)

admin.site.register(Editora, EditoraAdmin)