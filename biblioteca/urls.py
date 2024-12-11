from django.urls import path
from .views import *

urlpatterns = [
    
    path('', home, name='home'),
    
    path('registro', cria_user, name='registro'),
    path('accounts/logout', user_logout, name='logout'),
    
    path('autores/', lista_autores, name='lista_autores'),
    path('autores/criar/', criar_autor, name='criar_autor'),
    path('autores/<int:pk>/atualizar/', atualizar_autor, name='atualizar_autor'),
    path('autores/<int:pk>/deletar/', deletar_autor, name='deletar_autor'),
    
    
    path('editoras/', lista_editoras, name='lista_editoras'),
    path('editoras/criar/', criar_editora, name='criar_editora'),
    path('editoras/<int:pk>/atualizar/', atualizar_editora, name='atualizar_editora'),
    path('editoras/<int:pk>/deletar/', deletar_editora, name='deletar_editora'),
    
    
    path('generos/', lista_generos, name='lista_generos'),
    path('generos/criar/', criar_genero, name='criar_genero'),
    path('generos/<int:pk>/atualizar/', atualizar_genero, name='atualizar_genero'),
    path('generos/<int:pk>/deletar/', deletar_genero, name='deletar_genero'),
    
    
    path('livros/', lista_livros, name='lista_livros'),
    path('livros/criar/', criar_livro, name='criar_livro'),
    path('livros/<int:pk>/atualizar/', atualizar_livro, name='atualizar_livro'),
    path('livros/<int:pk>/deletar/', deletar_livro, name='deletar_livro'),
    
    
    path('leitores/', lista_leitores, name='lista_leitores'),
    path('leitores/criar/', criar_leitor, name='criar_leitor'),
    path('leitores/<int:pk>/atualizar/', atualizar_leitor, name='atualizar_leitor'),
    path('leitores/<int:pk>/deletar/', deletar_leitor, name='deletar_leitor'),
    
    path('emprestimos/', lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/criar/', criar_emprestimo, name='criar_emprestimo'),
    path('emprestimos/<int:pk>/atualizar/', atualizar_emprestimo, name='atualizar_emprestimo'),
    path('emprestimos/<int:pk>/deletar/', deletar_emprestimo, name='deletar_emprestimo'),
]