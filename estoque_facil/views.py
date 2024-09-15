from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

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

def listar_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos do banco de dados
    return render(request, 'listar_produtos.html', {'produtos': produtos})