from django.shortcuts import render

# Django library
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)

from .models import Autor, Libros

class ListaAutores(ListView):
    template_name = 'biblioteca/lista-autores.html'
    model = Autor
    context_object_name = 'autores'

class ListaLibrosAutores(ListView):
    """Vista para listar libros por Autor"""
    template_name = 'biblioteca/lista-libros.html'    
    context_object_name = 'libros'

    def get_queryset(self):
        # Identificar el autor
        id = self.kwargs['pk']
        # Filtro de libros
        lista = Libros.objects.filter(
            autor = id
        )
        # Devolver resultado
        return lista

class AddAutor(CreateView):
    """ Vista para registrar un nuevo Autor """
    template_name = "biblioteca/add-autor.html"
    model = Autor
    fields = ['nombre', 'nacionalidad']
    success_url = '/'
    
