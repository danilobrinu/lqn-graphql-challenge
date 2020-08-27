# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ..character.models import Character


class Human(Character):
    home_planet = models.CharField(max_length=150)
    friends = models.ManyToManyField("Human", blank=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Human:{self.id}>"
