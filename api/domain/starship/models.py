# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ...utils import BaseModel


class Starship(BaseModel):
    name = models.CharField(max_length=100)
    length = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<Starship:{self.id}>"
