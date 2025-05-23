from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='autor.nombre')
    # Campo adicional calculado. No existe en el modelo directamente.
    # Se usa para mostrar datos personalizados, como las reseñas recientes del libro.
    recent_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = '__all__'

    # Método que obtiene las 5 reseñas más recientes del libro
    def get_recent_reviews(self, obj):
        reviews = obj.resenas.order_by('-fecha')[:5]
        return ReviewSerializer(reviews, many=True).data
