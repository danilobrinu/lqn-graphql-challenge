# Built-in packages

# Third-party packages
from django.db import models

# Local packages
from api.utils.models import BaseModel
from api.domain.person.models import Person
from api.domain.planet.models import Planet


class Episode(BaseModel):
    title = models.CharField(max_length=100)
    opening_text = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey(
        Person, related_name="episodes_by_director", on_delete=models.CASCADE
    )
    producers = models.ManyToManyField(Person, related_name="episodes_by_producers")
    planets = models.ManyToManyField(Planet, related_name="episodes_by_planets")

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return f"<Episode:{self.id}>"
