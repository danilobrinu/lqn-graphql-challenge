# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ...utils import BaseModel
from ..episode.models import Episode


class Character(BaseModel):
    name = models.CharField(max_length=100)
    appears_in = models.ManyToManyField(Episode)
