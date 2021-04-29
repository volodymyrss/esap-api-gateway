"""
Django settings for esap project for testing (docker)
"""

from esap.settings.base import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'cie-((m#n$br$6l53yash45*2^mwuux*2u)bad5(0flx@krnj9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "https://sdc-dev.astron.nl","https://sdc.astron.nl","http://dop457.astron.nl",
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

# Application definition

# Database
DATABASE_ROUTERS = [
    'query.database_router.QueryRouter',
    'accounts.database_router.AccountsRouter',
    'staging.database_router.StagingRouter',
    'ida.database_router.IdaRouter',
    'rucio.database_router.RucioRouter',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/shared/esap_config.sqlite3',
    },
    'accounts': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/shared/esap_accounts_config.sqlite3',
    },
    'staging': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/shared/esap_staging_config.sqlite3',
    },
    'ida': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/shared/esap_ida_config.sqlite3',
    },
    'rucio': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/shared/esap_rucio_config.sqlite3',
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static_esap/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = os.environ['LOGIN_REDIRECT_URL']
LOGOUT_REDIRECT_URL = os.environ['LOGOUT_REDIRECT_URL']
LOGIN_REDIRECT_URL_FAILURE = os.environ['LOGIN_REDIRECT_URL_FAILURE']