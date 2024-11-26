from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Use an environment variable for security
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # Administração do Django.
    'django.contrib.auth',  # Autenticação.
    'django.contrib.contenttypes',  # Framework de tipos de conteúdo.
    'django.contrib.sessions',  # Gerenciamento de sessões.
    'django.contrib.messages',  # Sistema de mensagens.
    'django.contrib.staticfiles',  # Gerenciamento de arquivos estáticos.
    'core',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de template do Django.
        'DIRS': ['templates'],  # Diretório de templates personalizados.
        'APP_DIRS': True,  # Django procura templates dentro de cada aplicação.
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Adiciona variáveis de depuração.
                'django.template.context_processors.request',  # Adiciona 'request' ao contexto dos templates.
                'django.contrib.auth.context_processors.auth',  # Adiciona variáveis relacionadas à autenticação.
                'django.contrib.messages.context_processors.messages',  # Adiciona mensagens ao contexto dos templates.
            ],
        },
    },
]


WSGI_APPLICATION = 'sgo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalização
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'  # Código da língua.
TIME_ZONE = 'America/Sao_Paulo'  # Fuso horário.
USE_I18N = True  # Habilita internacionalização.
USE_TZ = True  # Habilita suporte a fuso horário.


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'  # A URL onde os arquivos estáticos serão acessíveis

# Configurações de arquivos estáticos para desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Caminho para a pasta de arquivos estáticos
]

# Para produção, descomente a linha abaixo:
# STATIC_ROOT = BASE_DIR / 'staticfiles'


# Configurações de autenticação e redirecionamento.
LOGIN_REDIRECT_URL = '/accounts/private_page_1/'  # Redirecionamento após login
LOGIN_URL = '/accounts/login'  # URL para página de login
LOGOUT_REDIRECT_URL = '/accounts/login'  # URL para redirecionar após logout


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email backend para desenvolvimento (no console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




