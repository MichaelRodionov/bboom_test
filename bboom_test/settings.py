"""Django settings for bboom_test project."""

from pathlib import Path

import environ


# ----------------------------------------------------------------
# environment settings
env = environ.Env(DEBUG=(bool, False))


# ----------------------------------------------------------------
# Build path settings
BASE_DIR = Path(__file__).resolve().parent.parent
env.read_env(BASE_DIR / '.env')


# ----------------------------------------------------------------
# Secret key settings
SECRET_KEY = env('SECRET_KEY')

# ----------------------------------------------------------------
# Debug settings
DEBUG = env('DEBUG')


# ----------------------------------------------------------------
# hosts settings
ALLOWED_HOSTS = ['*']


# ----------------------------------------------------------------
# Installed apps settings
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DRF_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
]

LOCAL_APPS = [
    'users',
    'posts',
    'ui',
]

INSTALLED_APPS = DJANGO_APPS + DRF_APPS + LOCAL_APPS


# ----------------------------------------------------------------
# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ----------------------------------------------------------------
# root urlconf settings
ROOT_URLCONF = 'bboom_test.urls'


# ----------------------------------------------------------------
# templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ----------------------------------------------------------------
# wsgi app settings
WSGI_APPLICATION = 'bboom_test.wsgi.application'


# ----------------------------------------------------------------
# Database settings
DATABASES = {
    'default': env.db()
}


# ----------------------------------------------------------------
# Password validation settings
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


# ----------------------------------------------------------------
# auth user model (custom auth model)
AUTH_USER_MODEL = 'users.User'


# ----------------------------------------------------------------
# Internationalization settings
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ----------------------------------------------------------------
# Static files (CSS, JavaScript, Images) settings
STATIC_URL = 'static/'


# ----------------------------------------------------------------
# Default primary key field type settings
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ----------------------------------------------------------------
# rest framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}


# ----------------------------------------------------------------
# spectacular settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'BBoom test application API',
    'DESCRIPTION': 'API for BBoom test project. Made by Michael Rodionov',
    'VERSION': '1.0.0'
}
