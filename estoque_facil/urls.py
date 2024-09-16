# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
]