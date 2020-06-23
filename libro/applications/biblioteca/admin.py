from django.contrib import admin

# Register your models here.
from .models import Autor, Libros

#Improving Authon Class
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #Field Search attribute
    search_fields = ('nombre', 'nacionalidad',)

#Improving Authon Class
class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'autor',
        'id'
    )
    #Field Search attribute
    search_fields = ('title',)
    #Filter Attribute
    list_filter = ('autor',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)