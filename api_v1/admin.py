from django.contrib import admin

# Register your models here.

from api_v1.domain.starship.models import Starship
from api_v1.domain.person.models import Person
from api_v1.domain.planet.models import Planet
from api_v1.domain.episode.models import Episode
from api_v1.domain.human.models import Human
from api_v1.domain.droid.models import Droid


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

