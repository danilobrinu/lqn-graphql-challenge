from django.contrib import admin

# Register your models here.

from api.domain.character.models import Character
from api.domain.starship.models import Starship
from api.domain.person.models import Person
from api.domain.planet.models import Planet
from api.domain.episode.models import Episode
from api.domain.human.models import Human
from api.domain.droid.models import Droid

admin.register(Character, Starship, Person, Planet, Episode, Human, Droid)
