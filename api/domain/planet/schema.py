# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.planet import models, types
from api.domain.planet.data import create_planet, update_planet, delete_planet


class CreatePlanet(types.PlanetOutputMutation, Mutation):
    class Arguments:
        data = types.PlanetCreateInput(required=True)

    @atomic
    @staticmethod
    def mutate(_, info: ResolveInfo, data: types.PlanetCreateInput) -> models.Planet:
        return create_planet(data)


class UpdatePlanet(types.PlanetOutputMutation, Mutation):
    class Arguments:
        data = types.PlanetUpdateInput(required=True)
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _,
        info: ResolveInfo,
        where: types.PlanetWhereUniqueInput,
        data: types.PlanetUpdateInput,
    ) -> models.Planet:
        return update_planet(where, data)


class DeletePlanet(types.PlanetOutputMutation, Mutation):
    class Arguments:
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _, info: ResolveInfo, where: types.PlanetWhereUniqueInput
    ) -> models.Planet:
        return delete_planet(where)


class PlanetQuery(ObjectType):
    planet = Node.Field(types.Planet)
    planets = types.PlanetFilterConnectionField(
        types.Planet, where=types.PlanetWhereInput()
    )


class PlanetMutation(ObjectType):
    create_planet = CreatePlanet.Field(required=True)
    update_planet = UpdatePlanet.Field()
    delete_planet = DeletePlanet.Field()
