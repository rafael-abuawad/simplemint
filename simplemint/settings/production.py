from decouple import config
import os

from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": "django",
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
        "OPTIONS": {"sslmode": "require"},
    }
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
