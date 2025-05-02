from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, BookSerializer, ReviewSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Activamos filtros por campos específicos del modelo (autor y fecha de publicación)
    filterset_fields = ['autor', 'fecha_publicacion']
    # Permitimos ordenar los resultados por título o fecha de publicación
    ordering_fields = ['titulo', 'fecha_publicacion']

    def get_queryset(self):
        if self.request.query_params.get('recent'):
            return Libro.objects.order_by('-fecha_publicacion')[:10]
        return super().get_queryset()

    # Ruta adicional que no forma parte del CRUD. Se usa para calcular
    # la calificación promedio de un libro específico.
    @action(detail=True, methods=['get'])
    def average_rating(self, request, pk=None):
        book = self.get_object()
        avg = book.resenas.aggregate(Avg('calificacion'))['calificacion__avg']
        return Response({'average_rating': avg})

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ReviewSerializer
