from django.contrib import admin
from .models import Libro, Genero, Autor

# Register your models here.
admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Autor)
