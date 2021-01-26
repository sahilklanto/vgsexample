from settings.base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vgsexample',
        'USER': 'postgres',
        'PASSWORD': 'postgres'
    }
}

ENDPOINT_URL = 'http://localhost:8000'
