# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ..character.models import Character


class Droid(Character):
    primary_function = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Droid:{self.id}>"
