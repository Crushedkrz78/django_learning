from django.contrib import admin

# Register your models here.
from .models import Autor, Libros

admin.site.register(Autor)
admin.site.register(Libros)