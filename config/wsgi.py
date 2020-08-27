"""
WSGI config for starwars_graphql project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import dotenv

from django.core.wsgi import get_wsgi_application

dotenv.load_dotenv()

ENVIRONMENT_MODULE = os.getenv("ENVIRONMENT_MODULE", "develop")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{ENVIRONMENT_MODULE}")

application = get_wsgi_application()
