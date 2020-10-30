# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from api_v1.domain.starship import models, types, filters, crud


class CreateStarship(types.StarshipOutputMutation, gql.Mutation):
    class Arguments:
        data = types.StarshipCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship, _info: gql.ResolveInfo, data: types.StarshipCreateInput
    ) -> models.Starship:
        return crud.create_starship(data)


class UpdateStarship(types.StarshipOutputMutation, gql.Mutation):
    class Arguments:
        where = types.StarshipWhereUniqueInput(required=True)
        data = types.StarshipUpdateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship,
        _info: gql.ResolveInfo,
        where: types.StarshipWhereUniqueInput,
        data: types.StarshipUpdateInput,
    ) -> models.Starship:
        return crud.update_starship(where, data)


class DeleteStarship(types.StarshipOutputMutation, gql.Mutation):
    class Arguments:
        where = types.StarshipWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship,
        _info: gql.ResolveInfo,
        where: types.StarshipWhereUniqueInput,
    ) -> models.Starship:
        return delete_starship(where)


class Query(gql.ObjectType):
    starship = gql.Field(
        types.Starship, where=types.StarshipWhereUniqueInput(required=True)
    )
    starships = gql.Field(
        gql.List(gql.NonNull(types.Starship)), where=types.StarshipWhereInput()
    )
    starshipsConnection = types.StarshipFilterConnectionField(
        types.Starship, where=types.StarshipWhereInput()
    )

    def resolve_starship(
        _root: models.Starship,
        _info: gql.ResolveInfo,
        where: types.StarshipWhereUniqueInput,
    ) -> models.Starship:
        return crud.get_starship(where)

    def resolve_starships(
        _root: models.Starship,
        _info: gql.ResolveInfo,
        where: types.StarshipWhereUniqueInput = None,
    ) -> list[models.Starship]:
        return crud.get_starships(where)


class Mutation(gql.ObjectType):
    create_starship = CreateStarship.Field(required=True)
    update_starship = UpdateStarship.Field()
    delete_starship = DeleteStarship.Field()
