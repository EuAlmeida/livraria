from django.db import models

from .autor import Autor
from .categoria import Categoria
from .editora import Editora

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=32, null= True, blank=True)
    quantidade = models.IntegerField(null=True)
    preço = models.DecimalField(decimal_places=2, max_digits=3, null= True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autor = models.ManyToManyField(Autor, related_name="Livro")

    def __str__(self):
        return f"{self.nome_livro}({self.editora})"