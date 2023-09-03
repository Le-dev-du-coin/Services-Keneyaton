from .base import *
import os
from decouple import config, Csv


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

""" DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": config("HOST"),
        "PORT": "",
    }
} """

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Static files (CSS, JavaScript, Images)

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = config("AWS_S3_SIGNATURE_NAME")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
#AWS_CUSTOM_DOMAIN = ''
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400', # 1 day
}
AWS_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_LOCATION = 'static'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_URL = "https://services-keneyaton.com/%s/" % AWS_LOCATION
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STORAGES = {"default": {"BACKEND": "store.custom_storage.MediaStorage"}}
STORAGES = {"staticfiles": {"BACKEND": "storages.backends.s3boto3.S3StaticStorage"}}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#Django sucure Configurations
SECURE_HSTS_SECONDS = 31536000  # 1 an
SECURE_SSL_REDIRECT=True   #https redirect
SESSION_COOKIE_SECURE = True    #session cookie secure
CSRF_COOKIE_SECURE = True      #csrfcookie secure
#X_FRAME_OPTIONS='SAMEORIGIN'#xframe options sameorigin

