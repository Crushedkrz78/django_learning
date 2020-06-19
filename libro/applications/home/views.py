from django.shortcuts import render

from django.views.generic import(
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    # Una vista procesa los datos y renderiza resultado en pantalla
    # Siempre se solicitara un Template
    # Un template es un archivo HTML
    template_name = "home/index.html"
    print("Home View Works!")

class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['El quijote', 'Codigo Limpio', 'La Sombra del Viento', 'Django 2.0']
    context_object_name = 'libros'

