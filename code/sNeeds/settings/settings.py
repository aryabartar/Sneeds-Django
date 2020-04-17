"""
Django settings for sNeeds project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# from .secure.APIs import dropbox_static_files_sneeds
#
# DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
# DROPBOX_OAUTH2_TOKEN = dropbox_static_files_sneeds
#
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "templates")

INSTALLED_APPS = [
    'rest_framework',
    'django_filters',  # for filtering get queries in DRF
    'drf_yasg',  # for filtering get queries in DRF
    'django_rest_passwordreset',
    'polymorphic',  # For django-polymorphic
    'ckeditor',

    'sNeeds.apps.customAuth',
    'sNeeds.apps.account',
    'sNeeds.apps.consultants',
    'sNeeds.apps.store',
    'sNeeds.apps.docs',
    'sNeeds.apps.carts',
    'sNeeds.apps.orders',
    'sNeeds.apps.comments',
    'sNeeds.apps.payments',
    'sNeeds.apps.userfiles',
    'sNeeds.apps.discounts',
    'sNeeds.apps.videochats',
    'sNeeds.apps.chats',
    'sNeeds.apps.storePackages',
    'sNeeds.apps.customUtils',
    'sNeeds.apps.basicProducts',
    'sNeeds.apps.customForms',

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'dbbackup',
    'django_cleanup',  # should go after your apps
]
# Imported key to prevent circular imports.
from .secure import keys

SECRET_KEY = os.environ.get('SECRET_KEY')

ROOT_URLCONF = 'sNeeds.urls'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # For per-request translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'sNeeds.settings.middlewares.middlewares.CORSMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'sNeeds.wsgi.application'

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_TZ = True
TIME_ZONE = 'Asia/Tehran'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "..", "files"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "..", 'static')

MEDIA_URL = '/files/'
MEDIA_ROOT = 'files'

AUTH_USER_MODEL = 'customAuth.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 8,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'EXCEPTION_HANDLER': 'sNeeds.utils.custom.exception_handler.exception_handler',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST_IP'),
        'PORT': os.environ.get('DB_HOST_PORT'),
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, '..', 'translations'),
]

from .config.JWTAuthConfig import JWT_AUTH

# Loading API keys
from .celery.celery_config import *

# APIs
from .secure import APIs

SKYROOM_API_KEY = APIs.skyroom
SENDINBLUE_API_KEY = APIs.sendinblue
ZARINPAL_MERCHANT = APIs.zarinpal_merchant

# Keys
ALL_SKYROOM_USERS_PASSWORD = keys.ALL_SKYROOM_USERS_PASSWORD

# CORS
from corsheaders.defaults import default_headers

# TODO: Make this accurate
CORS_ALLOW_HEADERS = list(default_headers) + [
    'CLIENT-TIMEZONE',
    'CLIENT_TIMEZONE',
    'HTTP-CLIENT-TIMEZONE',
    'HTTP_CLIENT_TIMEZONE',
    'HTTP_CLIENT-TIMEZONE',
    'authorization',
    'AUTHORIZATION',
    'Authorization'
]

# dbbackup -------
from .secure.APIs import dropbox_sneeds_backups_app

DBBACKUP_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': dropbox_sneeds_backups_app,
}
# TODO: Add PGP encryption.
# ---------------------


# ---------------------
# Because of OPTIONS
# https://github.com/encode/django-rest-framework/issues/5616
from rest_framework import permissions
from sNeeds.utils.custom.custom_permissions import CustomIsAuthenticated

permissions.IsAuthenticated = CustomIsAuthenticated
# ---------------------
