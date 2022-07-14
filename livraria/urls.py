from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.serializers import AutorSerializer
from core.views import AutorViewSet, CategoriaViewset, EditoraViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewset)
router.register(r'editora', EditoraViewSet)
router.register(r'autor', AutorViewSet)
router.register(r'Livro', LivroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
