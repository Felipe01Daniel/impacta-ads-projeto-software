from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import UserForm, UserProfileForm
from django.contrib import messages
from .forms import ProdutoForm
from .models import Produto, Categoria

# Create your views here.
def is_admin(user):
    return user.is_superuser

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto criado com sucesso!')
            return redirect('adicionar_produto') 
    else:
        form = ProdutoForm()
    
    return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

def listar_produtos(request):
    nome_query = request.GET.get('nome', '')
    categoria_query = request.GET.get('categoria', '')

    produtos = Produto.objects.all()

    # Filtro por nome
    if nome_query:
        produtos = produtos.filter(nome__icontains=nome_query)

    # Filtro por categoria
    if categoria_query:
        produtos = produtos.filter(categoria__id=categoria_query)

    categorias = Categoria.objects.all()
    return render(request, 'listar_produtos.html', {
        'produtos': produtos,
        'categorias': categorias,
        'nome_query': nome_query,
        'categoria_query': categoria_query
    })

@user_passes_test(is_admin)
def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('listar_produtos') 
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'create_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listar_produtos') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso!')
    return redirect('login')