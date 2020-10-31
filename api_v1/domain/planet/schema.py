# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from api_v1.domain.planet import models, types, crud


class CreatePlanet(types.PlanetOutputMutation, gql.Mutation):
    class Arguments:
        data = types.PlanetCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Planet, _info: gql.ResolveInfo, data: types.PlanetCreateInput
    ) -> models.Planet:
        return crud.create_planet(data)


class UpdatePlanet(types.PlanetOutputMutation, gql.Mutation):
    class Arguments:
        data = types.PlanetUpdateInput(required=True)
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Planet,
        _info: gql.ResolveInfo,
        where: types.PlanetWhereUniqueInput,
        data: types.PlanetUpdateInput,
    ) -> models.Planet:
        return crud.update_planet(where, data)


class DeletePlanet(types.PlanetOutputMutation, gql.Mutation):
    class Arguments:
        where = types.PlanetWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Planet,
        _info: gql.ResolveInfo,
        where: types.PlanetWhereUniqueInput,
    ) -> models.Planet:
        return crud.delete_planet(where)


class Query(gql.ObjectType):
    planet = gql.Field(types.Planet)
    planets = types.PlanetFilterConnectionField(
        types.Planet, where=types.PlanetWhereInput()
    )

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_planet(
        _root: models.Planet,
        _info: gql.ResolveInfo,
        where: types.PlanetWhereUniqueInput,
    ) -> models.Planet:
        return crud.get_planet(where)

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_planets(
        _root: models.Planet, _info: gql.ResolveInfo, where: types.PlanetWhereInput
    ) -> list[models.Planet]:
        return crud.get_planets(where)


class Mutation(gql.ObjectType):
    create_planet = CreatePlanet.Field(required=True)
    update_planet = UpdatePlanet.Field()
    delete_planet = DeletePlanet.Field()
