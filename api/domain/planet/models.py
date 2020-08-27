# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ...utils import BaseModel


class Planet(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Planet:{self.id}>"
