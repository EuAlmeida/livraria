from ftplib import MAXLINE
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome_autor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_autor
    class Meta:
        verbose_name_plural = 'Autores'


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


    


