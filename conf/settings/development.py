from conf.settings.base import *

DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR.joinpath('db.sqlite3')),
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]


MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]