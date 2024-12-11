from django.contrib import admin
from .models import Autor, Editora, Genero, Livro, Leitor, Emprestimo

# Register your models here.

admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Genero)
admin.site.register(Livro)
admin.site.register(Leitor)
admin.site.register(Emprestimo)