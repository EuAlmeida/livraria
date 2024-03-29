from django.db import models

from uploader.models import Image

from .autor import Autor
from .categoria import Categoria
from .editora import Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=150, null=False, blank=False)
    isbn = models.CharField(max_length=32, null= True, blank=True)
    quantidade = models.IntegerField(null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=7, null= True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
    autores = models.ManyToManyField(Autor, related_name="Livro")
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.nome_livro}({self.editora})"