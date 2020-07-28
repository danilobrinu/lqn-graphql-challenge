# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation
from graphene.relay import Node

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import types
from . import filters

from .data import get_planet, create_planet, update_planet, delete_planet


class CreatePlanet(types.PlanetOutputMutation, Mutation):
    class Input:
        data = types.PlanetCreateInput(required=True)

    @atomic
    def mutate(self, info, data: types.PlanetCreateInput):
        return create_planet(data)


class UpdatePlanet(types.PlanetOutputMutation, Mutation):
    class Input:
        data = types.PlanetUpdateInput(required=True)
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    def mutate(
        self, info, where: types.PlanetWhereUniqueInput, data: types.PlanetUpdateInput,
    ):
        return update_planet(where, data)


class DeletePlanet(types.PlanetOutputMutation, Mutation):
    class Input:
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, where: types.PlanetWhereUniqueInput):
        return delete_planet(where)


class PlanetQuery(ObjectType):
    planet = Node.Field(types.Planet)
    planets = types.PlanetFilterConnection(types.Planet, where=types.PlanetWhereInput())


class PlanetMutation(ObjectType):
    create_planet = CreatePlanet.Field(required=True)
    update_planet = UpdatePlanet.Field()
    delete_planet = DeletePlanet.Field()
