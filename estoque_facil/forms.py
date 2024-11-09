from django import forms
from django.contrib.auth.models import User
from .models import Produto, UserProfile

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade', 'preco', 'categoria']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Selecione uma categoria"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Nome de Usuário',
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'exemplo@impacta.com.br'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'profile_picture', 'date_of_birth', 'address', 'phone_number', 'level', 'status']
        labels = {
            'name': 'Nome Completo',
            'profile_picture': 'Foto de Perfil',
            'date_of_birth': 'Data de Nascimento',
            'address': 'Endereço',
            'phone_number': 'Telefone',
            'level': 'Nível',
            'status': 'Status',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'DD/MM/AAAA'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '(11) 91234-5678'}),
            'address': forms.TextInput(attrs={'placeholder': 'Rua, número, bairro, cidade, estado'}),
            'level': forms.NumberInput(attrs={'min': 0, 'max': 100, 'step': 1, 'placeholder': 'Ex: 50'}),
            'status': forms.Select(choices=[
                ('Colaborador', 'Colaborador'),
                ('Líder', 'Líder'),
                ('Gerente', 'Gerente'),
                ('Diretor', 'Diretor')
            ])
        }