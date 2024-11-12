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

     return render(request, 'core/cadastro.html', {'form': form})





