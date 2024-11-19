# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from .forms import LoginForm, CadastroForm

# def login_page(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         cpf = request.POST.get('cpf')
#         senha = request.POST.get('senha')
        
#         # Verifica se o e-mail e CPF foram preenchidos
#         if not email or not cpf or not senha:
#             messages.error(request, 'Por favor, preencha todos os campos.')
#             return render(request, 'core/cadastro.html', {'form': LoginForm()})
        
#         # Verifica se o usuário existe com o e-mail e o CPF
#         try:
#             usuario = User.objects.get(email=email, username=cpf)  # Verifica email e CPF
            
#             # Tenta autenticar com a senha fornecida
#             user = authenticate(request, username=usuario.username, password=senha)
            
#             if user is not None:
#                 # Se o usuário for autenticado, faz o login
#                 login(request, user)
#                 # Redireciona para a página inicial do usuário
#                 return redirect('hom')  # Certifique-se de que 'home_logado' está configurada nas URLs
                
#             else:
#                 # Se a senha estiver incorreta
#                 messages.error(request, 'Senha incorreta. Tente novamente.')
#                 return render(request, 'core/cadastro.html', {'error': 'Senha incorreta.', 'form': LoginForm()})
        
#         except User.DoesNotExist:
#             # Se o e-mail e o CPF não coincidirem com nenhum usuário no banco
#             messages.error(request, 'Usuário não encontrado. Por favor, faça o cadastro.')
#             return render(request, 'core/cadastro.html', {'error': 'Usuário não encontrado.', 'form': LoginForm()})
    
#     # Se a requisição for GET (exibe o formulário de login)
#     return render(request, 'core/cadastro.html', {'form': LoginForm()})

# # Função para cadastro de usuário
# def cadastro(request):
#     if request.method == 'POST':
#         form = CadastroForm(request.POST)
        
#         if form.is_valid():
#             # Cria o usuário com os dados fornecidos
#             usuario = form.save()
#             messages.success(request, 'Cadastro realizado com sucesso. Faça o login!')
#             return redirect('login')  # Redireciona para a página de login
        
#     else:
#         form = CadastroForm()

#     return render(request, 'core/cadastro.html', {'form': form})


# # Função para a página inicial após login
# def home_logado(request):
#     if not request.user.is_authenticated:
#         return redirect('login')  # Se o usuário não estiver logado, redireciona para o login

#     nome = request.user.first_name  # Pega o primeiro nome do usuário logado
#     return render(request, 'core/home_logado.html', {'nome': nome})


# # Função para a página de "Sobre nós"
# def sobrenos(request):
#     return render(request, 'core/sobrenos.html')

# # Função para a página de "Tratamentos"
# def tratamentos(request):
#     return render(request, 'core/tratamentos.html')

# # Função para a página de "Tecnologias"
# def tecnologias(request):
#     return render(request, 'core/tecnologias.html')

# # Função para a página de "Consultório"
# def consultorio(request):
#     return render(request, 'core/consultorio.html')

# def home(request):
#     return render(request, 'core/home.html')

# def criar_usuario(request):
#     return render(request, 'core/criar_usuario.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.hashers import check_password
from .forms import UsuarioForm
from .models import Usuario
from .forms import LoginForm
from django.contrib import messages


# Create your views here.
 # Importa o decorador login_required

####@login_required  # Protege a view home para que apenas usuários autenticados possam acessá-la
def home(request):
    return render(request, 'core/home.html')  # Renderiza o template home.html

def home_logado(request):
    return render(request, 'core/home_logado.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'core/cadastro.html')  # Renderiza o template cadastro.html

def tratamentos(request):
    return render(request, 'core/tratamentos.html')  # Renderiza o template cadastro.html

def tecnologias(request):
    return render(request, 'core/tecnologias.html')  # Renderiza o template cadastro.html

def sobrenos(request):
    return render(request, 'core/sobrenos.html')  # Renderiza o template cadastro.html

def consultorio(request):
    return render(request, 'core/consultorio.html')  # Renderiza o template cadastro.html

def home_medico(request):
    return render(request, 'core/home_medico.html')  # Renderiza o template cadastro.html

def criar_usuario(request):
     if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data.get('cpf')

            if Usuario.objects.filter(cpf=cpf).exists():
                messages.error(request, 'CPF já cadastrado.')
                return redirect('cadastro')

            form.save()
            return redirect('teste')

     else:
         form = UsuarioForm()

     return render(request, 'core/login.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            cpf = form.cleaned_data['cpf']
            try:
                usuario = Usuario.objects.get(email=email, cpf=cpf)
            # Pega o nome associado ao CPF e email
                nome = usuario.nome.split()[0]
                return render(request, 'core/home_logado.html', {'nomes': [nome]})

            except Usuario.DoesNotExist:
                return redirect('cadastro')
    else:
        form = LoginForm()
    
    return render(request, 'core/home.html', {'form': form})

