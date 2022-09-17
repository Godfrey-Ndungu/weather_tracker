from .base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('NAME'),
        'USER':config('NAME'),
        'PASSWORD':config('PASSWORD'),
        'HOST':config('HOST'),
        'PORT': '',
    }
}
