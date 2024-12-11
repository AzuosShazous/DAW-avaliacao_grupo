from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome



class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    ano_publicacao = models.IntegerField()
    autores = models.ManyToManyField(Autor)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo



class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    leitor = models.ForeignKey(Leitor, on_delete=models.SET_NULL, null=True)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()

    def __str__(self):
        return f"{self.livro} emprestado por {self.leitor}"
