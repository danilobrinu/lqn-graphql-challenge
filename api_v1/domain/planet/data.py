# Built-in packages
from typing import Union

# Third-party packages
import graphql_relay as relay_gql

# Local packages
from api_v1.domain.planet import models, types, serializers


def create_planet(data: types.PlanetCreateInput) -> models.Planet:
    serializer = serializers.PlanetSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return serializer.instance


def get_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    _, planet_id = relay_gql.from_global_id(where.get())
    planet = models.Planet.objects.get(id=planet_id)

    return planet


def update_planet(
    where: types.PlanetWhereUniqueInput, data: types.PlanetUpdateInput
) -> models.Planet:
    planet = get_planet(where)
    serializer = serializers.PlanetSerializer(planet, data=data, partial=True)
    serializer.save()

    return serializer.instance


def delete_planet(where: types.PlanetWhereUniqueInput) -> models.Planet:
    planet = get_planet(where)
    planet.delete()

    return planet
