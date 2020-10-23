# Built-in packages
from typing import Union

# Third-party packages
from graphql_relay import from_global_id

# Local packages
from api.domain.planet import models, types


def create_planet(data: types.PlanetCreateInput) -> models.Planet:
    created_planet = models.Planet(**data).create()
    return created_planet


def get_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    _, planet_id = from_global_id(where.get())
    planet = models.Planet.objects.get(id=planet_id)
    return planet


def update_planet(
    where: types.PlanetWhereUniqueInput, data: types.PlanetUpdateInput
) -> models.Planet:
    updated_planet = get_planet(where).update(**data)
    return updated_planet


def delete_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    deleted_planet = get_planet(where).destroy()
    return deleted_planet
