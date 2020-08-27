"""
ASGI config for starwars_graphql project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import dotenv

from django.core.asgi import get_asgi_application

dotenv.load_dotenv()

ENVIRONMENT_MODULE = os.getenv("ENVIRONMENT_MODULE", "develop")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"config.settings.{ENVIRONMENT_MODULE}")

application = get_asgi_application()
