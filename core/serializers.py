from dataclasses import field
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Livro 

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


from core.models import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

from core.models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

