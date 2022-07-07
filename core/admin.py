from django.contrib import admin

from core.models import Categoria, Livro, Autor, Editora
admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Editora)

