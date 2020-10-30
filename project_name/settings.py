"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

# python
import ast
import os

from pathlib import Path

# django
from django.utils.translation import ugettext_lazy as _

# third party
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key
SECRET_KEY = os.getenv('SECRET_KEY', '0oew=(&hwcs5z_j1u#kyc&70+azsmxtct29!_xv#()*4=3=kvw')

# SECURITY WARNING: don't run with debug turned on in production!
# https://docs.djangoproject.com/en/3.1/ref/settings/#debug
DEBUG = ast.literal_eval(os.getenv('DEBUG', 'True'))

HOME_DIR = '/tmp' if DEBUG else os.path.expanduser('~')

ALLOWED_HOSTS = [
    'localhost',
] if DEBUG else [

]


# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # third party
    'django_extensions',

    # project
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

ROOT_URLCONF = 'project_name.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'project_name.wsgi.application'


# ### DATABASE ###
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     os.getenv('DATABASE_NAME',     'db'),
        'USER':     os.getenv('DATABASE_USER',     'user'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'pass'),
        'HOST':     os.getenv('DATABASE_HOST',     '127.0.0.1'),
        'PORT':     os.getenv('DATABASE_PORT',     '5432')
    }
}


# ### EMAIL ###

# https://docs.djangoproject.com/en/3.1/ref/settings/#email-host
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')

# https://docs.djangoproject.com/en/3.1/ref/settings/#default-from-email
# DEFAULT_FROM_EMAIL = ''

# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SERVER_EMAIL
# SERVER_EMAIL = DEFAULT_FROM_EMAIL


# ### AUTH ###

# https://docs.djangoproject.com/en/3.1/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [

    # Django ModelBackend is the default authentication backend.
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
]

# https://docs.djangoproject.com/en/3.1/ref/settings/#login-redirect-url
# LOGIN_REDIRECT_URL = ''

# https://docs.djangoproject.com/en/3.1/ref/settings/#login-url
# LOGIN_URL = ''

# https://docs.djangoproject.com/en/3.1/ref/settings/#logout-redirect-url
# LOGOUT_REDIRECT_URL = ''

# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]


# ### SECURITY ###

# https://docs.djangoproject.com/en/3.1/ref/settings/#secure-proxy-ssl-header
SECURE_PROXY_SSL_HEADER = None if DEBUG else ('HTTP_X_FORWARDED_PROTO', 'https')


# https://docs.djangoproject.com/en/3.1/ref/settings/#use-x-forwarded-host
USE_X_FORWARDED_HOST = False if DEBUG else True

# https://docs.djangoproject.com/en/3.1/ref/settings/#use-x-forwarded-port
USE_X_FORWARDED_PORT = False if DEBUG else True


# ### SESSIONS ###

# https://docs.djangoproject.com/en/3.1/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = False if DEBUG else True

# https://docs.djangoproject.com/en/3.1/ref/settings/#session-engine
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# https://docs.djangoproject.com/en/3.1/ref/settings/#session-expire-at-browser-close
SESSION_EXPIRE_AT_BROWSER_CLOSE = False if DEBUG else True


# ### INTERNATIONALIZATION ###
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# https://docs.djangoproject.com/en/3.1/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# https://docs.djangoproject.com/en/3.1/ref/settings/#languages
LANGUAGE_PT_BR = 'pt-br'
LANGUAGE_EN = 'en-us'
LANGUAGE_ES = 'es'

LANGUAGES = [
    (LANGUAGE_PT_BR, _('Brazilian Portuguese')),
    (LANGUAGE_EN,    _('English')),
    (LANGUAGE_ES,    _('Spanish'))
]

# https://docs.djangoproject.com/en/3.1/ref/settings/#locale-paths
LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

# https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/3.1/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/3.1/ref/settings/#use-tz
USE_TZ = True


# ### STATIC FILES (CSS, JavaScript, Images) ###
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# https://docs.djangoproject.com/en/3.1/ref/settings/#static-root
STATIC_ROOT_PATH = 'static/'
STATIC_ROOT = None if DEBUG else HOME_DIR / STATIC_ROOT_PATH

# https://docs.djangoproject.com/en/3.1/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/3.1/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]

# https://docs.djangoproject.com/en/2.2/ref/settings/#managers
MANAGERS = ADMINS

HOME = '/tmp' if DEBUG else os.path.expanduser('~')

# ### MEDIA ###

# https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_BASE_DIR = BASE_DIR if DEBUG else HOME
MEDIA_ROOT_PATH = 'media/'
PRIVATE_MEDIA_ROOT_PATH = 'media_private/'
MEDIA_ROOT = os.path.join(MEDIA_BASE_DIR, MEDIA_ROOT_PATH)
PRIVATE_MEDIA_ROOT = os.path.join(MEDIA_BASE_DIR, PRIVATE_MEDIA_ROOT_PATH)

# https://docs.djangoproject.com/en/2.2/ref/settings/#meda-iurl
MEDIA_URL = '/media/'