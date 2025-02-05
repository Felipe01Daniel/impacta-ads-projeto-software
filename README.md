# Software Product: Analysis, Specication, Project & Implementation

## 📌 Sobre o Projeto
Este é um **Sistema de Gerenciamento de Estoque** desenvolvido como parte do projeto da disciplina de **Software Product: Analysis, Specication, Project & Implementation** no curso de **Análise e Desenvolvimento de Sistemas** da **Faculdade Impacta**. O sistema permite o controle eficiente de produtos, incluindo cadastro, edição, remoção e acompanhamento do histórico de entrada e saída.

## 🚀 Tecnologias Utilizadas
O projeto foi desenvolvido utilizando as seguintes tecnologias:
- **Back-end:** Django (Python)
- **Banco de Dados:** PostgreSQL
- **Front-end:** HTML, CSS, JavaScript
- **Gerenciamento de Dependências:** pip e virtualenv
- **Controle de Versão:** Git e GitHub

## 🔧 Funcionalidades
✅ Cadastro de produtos no estoque  
✅ Listagem de produtos cadastrados  
✅ Edição e remoção de produtos  
✅ Filtro para busca de produtos  
✅ Controle de entrada e saída de produtos  
✅ Histórico detalhado de movimentações no estoque  
✅ Sistema de autenticação para controle de acesso  

## 📂 Estrutura do Projeto
```
impacta-ads-projeto-software/
│-- manage.py
│-- requirements.txt
│-- config/   # Configurações do Django
│-- estoque/  # Aplicação principal
│   │-- models.py  # Modelos do banco de dados
│   │-- views.py   # Lógica das views
│   │-- urls.py    # Rotas do sistema
│   │-- templates/ # Arquivos HTML
│   │-- static/    # Arquivos CSS e JS
│-- db.sqlite3  # Banco de dados local (se usado SQLite para testes)
```

## 🛠️ Como Executar o Projeto
### 🔹 Pré-requisitos
Antes de começar, você precisará ter instalado:
- **Python 3.x**
- **PostgreSQL**
- **Virtualenv**

### 🔹 Passos para Rodar o Projeto
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/impacta-ads-projeto-software.git
   cd impacta-ads-projeto-software
   ```
2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure o banco de dados PostgreSQL** no arquivo `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'nome_do_banco',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
5. **Aplique as migrações e inicie o servidor:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
6. **Acesse o sistema em:**  
   ```
   http://127.0.0.1:8000/
   ```

## 🤝 Contribuição
Se quiser contribuir com melhorias, siga estes passos:
1. Faça um **fork** do repositório
2. Crie uma nova **branch** para sua funcionalidade (`git checkout -b minha-feature`)
3. Faça as alterações e **commite** (`git commit -m 'Minha nova funcionalidade'`)
4. Envie para o GitHub (`git push origin minha-feature`)
5. Abra um **Pull Request** 🚀

## 📄 Licença
Este projeto está sob a licença **MIT**. Você pode ver mais detalhes no arquivo `LICENSE`.

---

💡 **Desenvolvido por Felipe Daniel** | Faculdade Impacta 🎓
