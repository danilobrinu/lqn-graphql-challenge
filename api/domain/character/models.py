from django.db import models

from ..episode.models import Episode


class Character(models.Model):
    name = models.CharField(max_length=100)
    appears_in = models.ManyToManyField(Episode)

    class Meta:
        abstract = True
