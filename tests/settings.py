# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "*h14$myj*sps)85nom$z2477ildyz=ahslv5ghfjkse51yw5ba5c@wa8"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_postgres_utils",
]

SITE_ID = 1

if django.VERSION >= (1, 11):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
