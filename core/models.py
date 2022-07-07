from ftplib import MAXLINE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Livro(models.Model):
    nome_livro = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=20)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

    def __str__(self):
        return self.nome_livro


class Autor(models.Model):
    nome_autor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_autor
    class Meta:
        verbose_name_plural = 'Autores'