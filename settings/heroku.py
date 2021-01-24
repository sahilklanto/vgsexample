from settings.dev import ALLOWED_HOSTS
from settings.base import *
import os
import dj_database_url 

DEBUG = False

ALLOWED_HOSTS = ['vgsexample.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}