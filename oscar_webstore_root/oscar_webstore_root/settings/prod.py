# settings.local.py
from .base import *

import json
from django.core.exceptions import ImproperlyConfigured

# JSON based secrets module
with open(BASE_DIR.child("prod_secrets.json")) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrests=secrets):
    """Get the secret variable or return explicit exception"""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST': get_secret("DATABASE_HOST"),
        'PORT': '',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

OSCAR_SHOP_NAME = "VG2"

EMAIL_HOST = get_secret("EMAIL_HOST")
EMAIL_PORT = 1025