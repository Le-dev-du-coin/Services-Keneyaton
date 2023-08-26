from .base import *
import os
from decouple import config, Csv

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []




# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
    os.path.join(BASE_DIR, 'media/')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')