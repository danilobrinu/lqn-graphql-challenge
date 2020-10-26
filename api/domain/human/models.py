# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from api.domain.character.models import Character


class Human(Character):
    home_planet = models.CharField(max_length=150)
    friends = models.ManyToManyField(
        "Human", related_name="friends_by_human", blank=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.id}>"
