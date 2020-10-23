# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from api.utils.models import BaseModel
from api.domain.episode.models import Episode


class Character(BaseModel):
    name = models.CharField(max_length=100)
    appears_in = models.ManyToManyField(Episode, related_name="episodes_by_character")

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}:{self.id}"
