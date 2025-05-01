from django.contrib import admin
from django.urls import path, include  # ⬅️ importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('biblioteca.urls')),  # ⬅️ esto conecta las rutas de tu app
]
