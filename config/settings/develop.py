# Built-in package
import os

# Third-party packages

# Local packages
# skipcq: PYL-W0614
from .common import *  # noqa
from .common import BASE_DIR

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.develop.sqlite3"),
    }
}
