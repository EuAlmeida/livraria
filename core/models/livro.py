from django.db import models

from .autor import Autor
from .categoria import Categoria
from .editora import Editora

class Livro(models.Model):
    nome_livro = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20, null= True, blank=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    quantidade = models.IntegerField(null=True)
    preço = models.DecimalField(decimal_places=2, max_digits=3, null= True)

    def __str__(self):
        return self.nome_livro