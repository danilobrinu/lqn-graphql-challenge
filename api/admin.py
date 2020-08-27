from django.contrib import admin

# Register your models here.

from .domain.character.models import Character
from .domain.starship.models import Starship
from .domain.person.models import Person
from .domain.planet.models import Planet
from .domain.episode.models import Episode
from .domain.human.models import Human
from .domain.droid.models import Droid

admin.register(Character, Starship, Person, Planet, Episode, Human, Droid)
