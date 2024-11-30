from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpeg')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    level = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=50, default='Colaborador')

    def save(self, *args, **kwargs):

        # Lógica de status conforme o nível
        if self.level <= 10:
            self.status = 'Colaborador'
        elif self.level <= 40:
            self.status = 'Lider'
        elif self.level <= 50:
            self.status = 'Gerente'
        else:
            self.status = 'Diretor'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    
class Customer(models.Model):
    TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]

    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True) 
    company_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class SaidaProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.PositiveIntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_saida = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} para {self.cliente.name if self.cliente else 'Desconhecido'}"

    def save(self, *args, **kwargs):
        if self.quantidade > self.produto.quantidade:
            raise ValueError("Quantidade solicitada excede o estoque disponível.")
        self.valor_total = self.quantidade * self.produto.preco
        self.produto.quantidade -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)