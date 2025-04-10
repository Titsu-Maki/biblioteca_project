from django.utils import timezone
from biblioteca.models import Autor, Libro, Resena


autor1 = Autor.objects.create(nombre="Gabriel García Márquez", nacionalidad="Colombia")
autor2 = Autor.objects.create(nombre="Isabel Allende", nacionalidad="Chile")
autor3 = Autor.objects.create(nombre="Jorge Luis Borges", nacionalidad="Argentina")
autor4 = Autor.objects.create(nombre="Mario Vargas Llosa", nacionalidad="Peru")


libro1 = Libro.objects.create(titulo="Cien años de soledad", autor=autor1, fecha_publicacion="1967-06-05", resumen="Novela emblemática del realismo mágico.")
libro2 = Libro.objects.create(titulo="El amor en los tiempos del cólera", autor=autor1, fecha_publicacion="1985-09-05", resumen="Una historia de amor que resiste al paso del tiempo.")
libro3 = Libro.objects.create(titulo="La casa de los espíritus", autor=autor2, fecha_publicacion="1982-01-01", resumen="Una saga familiar con elementos sobrenaturales.")
libro4 = Libro.objects.create(titulo="Paula", autor=autor2, fecha_publicacion="1994-01-01", resumen="Una memoria personal y conmovedora.")
libro5 = Libro.objects.create(titulo="Ficciones", autor=autor3, fecha_publicacion="1944-01-01", resumen="Colección de cuentos filosóficos y fantásticos.")
libro6 = Libro.objects.create(titulo="El Aleph", autor=autor3, fecha_publicacion="1949-01-01", resumen="Cuentos que exploran el infinito y la percepción.")
libro7 = Libro.objects.create(titulo="La ciudad y los perros", autor=autor4, fecha_publicacion="1963-01-01", resumen="Crítica al sistema militar peruano.")
libro8 = Libro.objects.create(titulo="Conversación en La Catedral", autor=autor4, fecha_publicacion="1969-01-01", resumen="Retrato político y social del Perú.")
libro9 = Libro.objects.create(titulo="Del amor y otros demonios", autor=autor1, fecha_publicacion="1994-10-01", resumen="Historia de amor en tiempos coloniales.")
libro10 = Libro.objects.create(titulo="Retrato en sepia", autor=autor2, fecha_publicacion="2000-01-01", resumen="Novela histórica con tintes románticos.")

Resena.objects.create(libro=libro1, texto="Excelente libro, muy recomendado.", calificacion=5, fecha=timezone.now())
Resena.objects.create(libro=libro2, texto="Una historia profunda y conmovedora.", calificacion=4, fecha=timezone.now())
Resena.objects.create(libro=libro3, texto="Narrativa envolvente con personajes memorables.", calificacion=5, fecha=timezone.now())
Resena.objects.create(libro=libro4, texto="Un testimonio muy emotivo, aunque algo lento.", calificacion=3, fecha=timezone.now())
Resena.objects.create(libro=libro5, texto="Brillante, aunque complejo. No es para todos.", calificacion=4, fecha=timezone.now())
Resena.objects.create(libro=libro6, texto="Cuentos fascinantes con mucha carga filosófica.", calificacion=5, fecha=timezone.now())
Resena.objects.create(libro=libro7, texto="Crudo y realista, una lectura intensa.", calificacion=4, fecha=timezone.now())
Resena.objects.create(libro=libro8, texto="Requiere paciencia, pero vale la pena.", calificacion=3, fecha=timezone.now())
Resena.objects.create(libro=libro9, texto="Una historia corta pero impactante.", calificacion=4, fecha=timezone.now())
Resena.objects.create(libro=libro10, texto="Buena narrativa, aunque predecible en partes.", calificacion=3, fecha=timezone.now())