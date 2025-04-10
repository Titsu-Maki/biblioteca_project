# 📚 Proyecto Django - Biblioteca

Este es un proyecto web desarrollado con Django como parte de un ejercicio práctico. Permite registrar autores, libros y reseñas desde el panel de administración. El objetivo es familiarizarse con los modelos, el ORM, validaciones personalizadas y el uso del admin de Django.

---

## 🚀 Funcionalidades implementadas

- Registro y visualización de autores, libros y reseñas.
- Relaciones entre modelos (`Autor` ➝ `Libro` ➝ `Reseña`).
- Panel de administración personalizado.
- Script para poblar datos iniciales automáticamente.
- Validaciones personalizadas en los modelos:
  - Autor: el nombre no puede estar vacío.
  - Libro: el resumen debe tener mínimo 30 caracteres.
  - Reseña: calificación entre 1 y 5, con fecha de creación.

---

## 🧰 Requisitos

- Python 3.10 o superior
- pip
- Git (opcional)
- Entorno virtual (recomendado)

---

## ⚙️ Instalación y ejecución local

1. **Clona este repositorio:**

git clone https://github.com/Titsu-Maki/biblioteca_project.git

cd biblioteca_project


Crea y activa un entorno virtual:

python -m venv env


# En Windows:

env\Scripts\activate
# En Linux/Mac:

source env/bin/activate


Instala las dependencias:

pip install -r requirements.txt


Realiza las migraciones: 

python manage.py makemigrations

python manage.py migrate


Crea un superusuario para acceder al panel de administración:
python manage.py createsuperuser


Ejecuta el servidor:  

python manage.py runserver


Abre el navegador en:

http://127.0.0.1:8000/admin


(Opcional) Ejecuta el script para cargar datos iniciales:

python manage.py shell

>>> exec(open('poblar_datos.py').read())

![1](https://github.com/user-attachments/assets/aa44aa1f-7a47-442c-b250-67082ff636e6)
![2](https://github.com/user-attachments/assets/816440eb-ee2b-48e1-a728-0c80f522a901)
![3](https://github.com/user-attachments/assets/84ba9518-3609-48c7-8daa-9664a5a5566d)
![4](https://github.com/user-attachments/assets/f464b1d5-3150-44b1-85f3-050b2c9dd67a)
