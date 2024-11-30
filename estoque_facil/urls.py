# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_produto/', views.adicionar_produto, name='adicionar_produto'),
    path('listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('editar_produto/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('create-user/', views.create_user, name='create_user'),
    path('register-customer/',  views.register_customer, name='register_customer'),
    path('list-customers/', views.listar_clientes, name='listar_clientes'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]