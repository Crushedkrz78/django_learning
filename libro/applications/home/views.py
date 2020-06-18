from django.shortcuts import render

from django.views.generic import(
    TemplateView,
)

class IndexView(TemplateView):
    # Una vista procesa los datos y renderiza resultado en pantalla
    # Siempre se solicitara un Template
    # Un template es un archivo HTML
    template_name = "home/index.html"
    print("Home View Works!")

