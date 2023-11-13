import environ
import os

from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Initialise environment variables
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-6s8%%ya(bhh-cf=48j_0d#iqla-k@x5i1#eqv=k0$$om+sxi$&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
