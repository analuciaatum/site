# from django.urls import path  # Importa a função path para definir as rotas de URL
# from .views import home  # Importa a função de view 'home' do módulo 'views' local
# from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django
# from . import views
# # Lista de padrões de URL para a aplicação 'core'
# urlpatterns = [
#     # Define a rota para a página de login
#     # Utiliza a view LoginView padrão do Django, especificando o template 'login.html'
#     # O nome 'login' é usado para referenciar esta URL em outras partes do código, como templates e views
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     #page
#     path('teste/', views.login, name='teste'),

#     #page
#     path('cadastro/', views.cadastro, name='cadastro'),
#     #page
#     path('home_logado/', views.home_logado, name='home_logado'),

#     #page
#     path('', views.home, name='home'),

#     path('tratamentos/', views.tratamentos, name='tratamentos'),

#     #api
#     path('criar_usuario/', views.criar_usuario, name='criar_usuario'),


#     #api
#     path('tecnologias/', views.tecnologias, name='tecnologias'),

#     #api
#     path('sobrenos/', views.sobrenos, name='sobrenos'),

#     #api
#     path('consultorio/', views.consultorio, name='consultorio'),

    

     

    
    



    


   

#     # Define a rota para a raiz da aplicação ('/')
#     # Mapeia para a função de view 'home' importada do módulo 'views'
#     # Esta rota é nomeada 'home', permitindo sua referência fácil em outras partes do projeto
    


# ] 



from django.urls import path  # Importa a função path para definir as rotas de URL
from .views import home  # Importa a função de view 'home' do módulo 'views' local
from django.contrib.auth import views as auth_views  # Importa as views de autenticação do Django
from . import views
# Lista de padrões de URL para a aplicação 'core'
urlpatterns = [
    # Define a rota para a página de login
    # Utiliza a view LoginView padrão do Django, especificando o template 'login.html'
    # O nome 'login' é usado para referenciar esta URL em outras partes do código, como templates e views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #page
    path('teste/', views.login, name='teste'),

    #page
    path('cadastro/', views.cadastro, name='cadastro'),
    #page
    path('home_logado/', views.home_logado, name='home_logado'),

    #page
    path('', views.home, name='home'),

    path('tratamentos/', views.tratamentos, name='tratamentos'),

    #api
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),

  
    #api
    path('login_page/{id}', views.login_page, name='logado'),


    #api
    path('tecnologias/', views.tecnologias, name='tecnologias'),

    #api
    path('sobrenos/', views.sobrenos, name='sobrenos'),

    #api
    path('consultorio/', views.consultorio, name='consultorio'),

    path('home_medico/', views.home_medico, name='home_medico'),



    


   

    # Define a rota para a raiz da aplicação ('/')
    # Mapeia para a função de view 'home' importada do módulo 'views'
    # Esta rota é nomeada 'home', permitindo sua referência fácil em outras partes do projeto
    


]