from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto, Categoria

# Create your views here.
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionar_produto') 
    else:
        form = ProdutoForm()
    
    return render(request, 'adicionar_produto.html', {'form': form})

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