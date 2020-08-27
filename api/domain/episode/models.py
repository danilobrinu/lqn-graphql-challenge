# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from ..person.models import Person
from ..planet.models import Planet


class Episode(models.Model):
    title = models.CharField(max_length=100)
    opening_text = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(
        Person, related_name="episodes_by_director", on_delete=models.CASCADE
    )
    producers = models.ManyToManyField(Person, related_name="episodes_by_producers")
    planets = models.ManyToManyField(Planet, related_name="episodes_by_planets")

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"<Episode:{self.id}>"
