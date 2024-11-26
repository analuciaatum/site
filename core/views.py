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



from .models import Agendamento
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


def agendar_consulta(request):
    if request.method == 'POST':
        # Coletar os dados do formulário
        nome = request.POST['nome']
        email = request.POST['email']
        cpf = request.POST['cpf']
        data_nascimento = request.POST['data_nascimento']
        data_consulta = request.POST['data_consulta']
        tratamento = request.POST['tratamento']
        sexo = request.POST['sexo']
        medico = request.POST['medico']

        # Criar e salvar o agendamento no banco
        Agendamento.objects.create(
            nome=nome,
            email=email,
            cpf=cpf,
            data_nascimento=data_nascimento,
            data_consulta=data_consulta,
            tratamento=tratamento,
            sexo=sexo,
            medico=medico
        )

        # Adicionar uma mensagem de sucesso
        messages.success(request, 'Consulta agendada com sucesso!')

        # Redirecionar para a página "home_medico" após o agendamento
        return redirect('home_logado')  # O paciente volta para a página após agendar

    return render(request, 'home_logado.html')  # Se não for um POST, mostra o formulário


@login_required
def home_medico(request):
    # Pegar todos os agendamentos
    agendamentos = Agendamento.objects.all()

    return render(request, 'home_medico.html', {'agendamentos': agendamentos})




from django.contrib.auth import authenticate, login




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_doctor:
                    return redirect('home_medico')  # Redireciona para a página do médico
                else:
                    return redirect('home_paciente')  # Redireciona para a página do paciente
            else:
                form.add_error(None, 'Credenciais inválidas')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})





from django.shortcuts import render, get_object_or_404, redirect
from .models import Agendamento

from django.shortcuts import render, get_object_or_404

def editar_agendamento(request, id):
    # Obtemos o agendamento com o id fornecido ou 404 se não encontrado
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == "POST":
        # Aqui você deve tratar a atualização do agendamento com os dados enviados via POST
        agendamento.nome = request.POST.get('nome')
        agendamento.email = request.POST.get('email')
        agendamento.data_consulta = request.POST.get('data_consulta')
        agendamento.tratamento = request.POST.get('tratamento')

        agendamento.save()  # Salva as alterações no banco de dados

        return redirect('home_medico')  # Redireciona para a página principal após a edição

    return render(request, 'core/editar.html', {'agendamento': agendamento})



def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('home')  # Substitua 'home' pela URL correta da página inicial
    return render(request, 'excluir.html', {'agendamento': agendamento})







    