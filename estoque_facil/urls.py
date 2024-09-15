# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
]