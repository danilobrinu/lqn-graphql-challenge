from django.contrib import admin

# Register your models here.

from .domain.starship.models import Starship
from .domain.person.models import Person
from .domain.planet.models import Planet
from .domain.episode.models import Episode
from .domain.human.models import Human
from .domain.droid.models import Droid


@admin.register(Starship)
class StarshipAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    pass


@admin.register(Droid)
class DroidAdmin(admin.ModelAdmin):
    pass

