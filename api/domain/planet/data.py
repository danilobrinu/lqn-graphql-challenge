# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from . import models
from . import types


def create_planet(data: types.PlanetCreateInput) -> models.Planet:
    planet = models.Planet(**data)
    planet.save()
    return planet


def get_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    _, planet_id = from_global_id(where.get())
    planet = models.Planet.objects.get(id=planet_id)
    return planet


def update_planet(
    where: types.PlanetWhereUniqueInput, data: types.PlanetUpdateInput
) -> models.Planet:
    planet = get_planet(where)
    planet.update(**data)
    return planet


def delete_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    planet = get_planet(where)
    planet.delete()
    return planet
