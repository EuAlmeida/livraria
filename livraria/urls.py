from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from core.views import CategoriaViewset

router = DefaultRouter()
router.register(r'categorias', CategoriaViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
