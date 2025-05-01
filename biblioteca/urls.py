from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'libros', BookViewSet)
router.register(r'resenas', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]