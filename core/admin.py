from django.contrib import admin

from core.models import Autor, Categoria, Editora, Livro

admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Autor)
admin.site.register(Editora)



