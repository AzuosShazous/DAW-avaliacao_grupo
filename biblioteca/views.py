from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Editora, Genero, Livro, Leitor, Emprestimo
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def cria_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'registration/registro.html')

def user_logout(request):
    logout(request)
    return redirect('home')



@login_required
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})

def criar_autor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        nacionalidade = request.POST['nacionalidade']
        Autor.objects.create(nome=nome, data_nascimento=data_nascimento, nacionalidade=nacionalidade)
        return redirect('lista_autores')
    return render(request, 'form_autor.html')

def atualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.nome = request.POST['nome']
        autor.data_nascimento = request.POST['data_nascimento']
        autor.nacionalidade = request.POST['nacionalidade']
        autor.save()
        return redirect('lista_autores')
    return render(request, 'form_autor.html', {'autor': autor})

def deletar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'confirmar_deletar_autor.html', {'autor': autor})


@login_required
def lista_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'lista_editoras.html', {'editoras': editoras})

def criar_editora(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        endereco = request.POST['endereco']
        Editora.objects.create(nome=nome, endereco=endereco)
        return redirect('lista_editoras')
    return render(request, 'form_editora.html')

def atualizar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.nome = request.POST['nome']
        editora.endereco = request.POST['endereco']
        editora.save()
        return redirect('lista_editoras')
    return render(request, 'form_editora.html', {'editora': editora})

def deletar_editora(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        return redirect('lista_editoras')
    return render(request, 'confirmar_deletar_editora.html', {'editora': editora})


@login_required
def lista_generos(request):
    generos = Genero.objects.all()
    return render(request, 'lista_generos.html', {'generos': generos})

def criar_genero(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        Genero.objects.create(nome=nome)
        return redirect('lista_generos')
    return render(request, 'form_genero.html')

def atualizar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.nome = request.POST['nome']
        genero.save()
        return redirect('lista_generos')
    return render(request, 'form_genero.html', {'genero': genero})

def deletar_genero(request, pk):
    genero = get_object_or_404(Genero, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('lista_generos')
    return render(request, 'confirmar_deletar_genero.html', {'genero': genero})


@login_required
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})


def criar_livro(request):
    autores = Autor.objects.all()
    editoras = Editora.objects.all()
    generos = Genero.objects.all()

    if request.method == 'POST':
        titulo = request.POST['titulo']
        isbn = request.POST['isbn']
        ano_publicacao = request.POST['ano_publicacao']
        autores_ids = request.POST.getlist('autores')
        editora_id = request.POST['editora']
        genero_id = request.POST['genero']
        
        if editora_id == "":
            editora = None
        else:
            editora = get_object_or_404(Editora, pk=editora_id)
        
        if genero_id == "":
            genero = None
        else:
            genero = get_object_or_404(Genero, pk=genero_id)

        livro = Livro.objects.create(
            titulo=titulo, 
            isbn=isbn, 
            ano_publicacao=ano_publicacao, 
            editora=editora, 
            genero=genero
        )

        if autores_ids:
            livro.autores.set(autores_ids)
        
        livro.save()
        
        return redirect('lista_livros')

    return render(request, 'form_livro.html', {'autores': autores, 'editoras': editoras, 'generos': generos})




def atualizar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    autores = Autor.objects.all()
    editoras = Editora.objects.all()
    generos = Genero.objects.all()

    if request.method == 'POST':
        livro.titulo = request.POST['titulo']
        livro.isbn = request.POST['isbn']
        livro.ano_publicacao = request.POST['ano_publicacao']
        
        autores_ids = request.POST.getlist('autores')
        livro.autores.set(autores_ids)
        
        editora_id = request.POST['editora']
        if editora_id == "":
            livro.editora = None
        else:
            livro.editora = get_object_or_404(Editora, pk=editora_id)
        
        genero_id = request.POST['genero']
        if genero_id == "":
            livro.genero = None
        else:
            livro.genero = get_object_or_404(Genero, pk=genero_id)
        
        livro.save()
        return redirect('lista_livros')

    return render(request, 'form_livro.html', {
        'livro': livro,
        'autores': autores,
        'editoras': editoras,
        'generos': generos
    })


def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista_livros')
    return render(request, 'confirmar_deletar_livro.html', {'livro': livro})


@login_required
def lista_leitores(request):
    leitores = Leitor.objects.all()
    return render(request, 'lista_leitores.html', {'leitores': leitores})

def criar_leitor(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        data_nascimento = request.POST['data_nascimento']
        Leitor.objects.create(nome=nome, email=email, data_nascimento=data_nascimento)
        return redirect('lista_leitores')
    return render(request, 'form_leitor.html')

def atualizar_leitor(request, pk):
    leitor = get_object_or_404(Leitor, pk=pk)
    if request.method == 'POST':
        leitor.nome = request.POST['nome']
        leitor.email = request.POST['email']
        leitor.data_nascimento = request.POST['data_nascimento']
        leitor.save()
        return redirect('lista_leitores')
    return render(request, 'form_leitor.html', {'leitor': leitor})

def deletar_leitor(request, pk):
    leitor = get_object_or_404(Leitor, pk=pk)
    if request.method == 'POST':
        leitor.delete()
        return redirect('lista_leitores')
    return render(request, 'confirmar_deletar_leitor.html', {'leitor': leitor})


@login_required
def lista_emprestimos(request):
    emprestimos = Emprestimo.objects.all()
    return render(request, 'lista_emprestimos.html', {'emprestimos': emprestimos})

def criar_emprestimo(request):
    livros = Livro.objects.all()
    leitores = Leitor.objects.all()

    if request.method == 'POST':
        livro_id = request.POST['livro']
        leitor_id = request.POST['leitor']
        data_emprestimo = request.POST['data_emprestimo']
        data_devolucao = request.POST['data_devolucao']
        
        livro = get_object_or_404(Livro, pk=livro_id)
        leitor = get_object_or_404(Leitor, pk=leitor_id)
        
        Emprestimo.objects.create(
            livro=livro, 
            leitor=leitor, 
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )
        return redirect('lista_emprestimos')

    return render(request, 'form_emprestimo.html', {'livros': livros, 'leitores': leitores})

def atualizar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    livros = Livro.objects.all()
    leitores = Leitor.objects.all()

    if request.method == 'POST':
        emprestimo.livro = get_object_or_404(Livro, pk=request.POST['livro'])
        emprestimo.leitor = get_object_or_404(Leitor, pk=request.POST['leitor'])
        emprestimo.save()
        return redirect('lista_emprestimos')

    return render(request, 'form_emprestimo.html', {'emprestimo': emprestimo, 'livros': livros, 'leitores': leitores})

def deletar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('lista_emprestimos')
    return render(request, 'confirmar_deletar_emprestimo.html', {'emprestimo': emprestimo})