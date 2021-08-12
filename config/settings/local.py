from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'warehouse',
        'HOST': 'localhost',
    }
}

INSTALLED_APPS += ['debug_toolbar', ]
