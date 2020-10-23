# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from api.domain.character.models import Character


class Droid(Character):
    primary_function = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.id}>"
