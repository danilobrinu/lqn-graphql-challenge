# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from api.utils.models import BaseModel


class Planet(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.id}>"
