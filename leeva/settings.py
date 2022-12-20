
# BASIC CONFIGS

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!&(^1_a18^e@5h2pxlk*19i@3@9ai4!(y3j&-!5n(rx!7ln6hc'

DEBUG = False


# CONFIG HOSTS
ALLOWED_HOSTS = ["*"]


# INSTALLED APPS

SHARED_APPS = (
    'django_tenants',
    'tenant',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',

    'authentications', 
    'home',
)

TENANT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'companies',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]


# TENANTS
TENANT_MODEL = "tenant.Client"
TENANT_DOMAIN_MODEL = "tenant.Domain" 

# MIDLEWARES
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',

    'django.middleware.security.SecurityMiddleware',

    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'minuxdb',
        'USER': 'minux',
        'PASSWORD': 'MinuxDev',
        'PORT': '5432',
        'HOST': 'minuxdb.cn9nmk8zhjuk.ap-northeast-1.rds.amazonaws.com'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         'NAME': 'leevadb',
#         'USER': 'postgres',
#         'PASSWORD': 'minux',
#         'HOST': 'localhost'
#     }
# }

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)


# TEMPLATES

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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


# STATIC FILES
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'assets'
]

STATIC_URL = os.path.join(BASE_DIR,'staticfiles')


# OTHERS

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


ROOT_URLCONF = 'leeva.urls'

WSGI_APPLICATION = 'leeva.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CSRF_TRUSTED_ORIGINS = ['https://*.railway.app/','https://*.127.0.0.1']