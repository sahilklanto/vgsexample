from settings.dev import ALLOWED_HOSTS
from settings.base import *
import os
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['vgsexample.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

ENDPOINT_URL = 'https://vgsendpoint.herokuapp.com/api/v1/dummy-view'
