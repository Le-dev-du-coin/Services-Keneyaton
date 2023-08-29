from .base import *
import os
from decouple import config, Csv


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("PROD_DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("NAME"),
        "USER": config("USER"),
        "PASSWORD": config("PASSWORD"),
        "HOST": config("HOST"),
        "PORT": config("PORT"),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"


STATICFILES_DIRS = [os.path.join(BASE_DIR, "static/"), os.path.join(BASE_DIR, "media/")]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = config("AWS_S3_SIGNATURE_NAME")
AWS_S3_REGION_NAME = config("AWS_S3_REGION_NAME")
AWS_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
