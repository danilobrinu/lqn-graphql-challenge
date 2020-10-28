# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import Field, List, NonNull, ObjectType, Mutation, ResolveInfo

# Local packages
from api_v1.domain.starship import models, types, filters
from api_v1.domain.starship.data import (
    get_starship,
    create_starship,
    update_starship,
    delete_starship,
)


class CreateStarship(types.StarshipOutputMutation, Mutation):
    class Arguments:
        data = types.StarshipCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship, _info: ResolveInfo, data: types.StarshipCreateInput
    ) -> models.Starship:
        return create_starship(data)


class UpdateStarship(types.StarshipOutputMutation, Mutation):
    class Arguments:
        where = types.StarshipWhereUniqueInput(required=True)
        data = types.StarshipUpdateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship,
        _info: ResolveInfo,
        where: types.StarshipWhereUniqueInput,
        data: types.StarshipUpdateInput,
    ) -> models.Starship:
        return update_starship(where, data)


class DeleteStarship(types.StarshipOutputMutation, Mutation):
    class Arguments:
        where = types.StarshipWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Starship,
        _info: ResolveInfo,
        where: types.StarshipWhereUniqueInput,
    ) -> models.Starship:
        return delete_starship(where)


class Query(ObjectType):
    starship = Field(
        types.Starship, where=types.StarshipWhereUniqueInput(required=True)
    )
    starships = Field(List(NonNull(types.Starship)), where=types.StarshipWhereInput())
    starshipsConnection = types.StarshipFilterConnectionField(
        types.Starship, where=types.StarshipWhereInput()
    )

    def resolve_starships(
        _root: models.Starship,
        _info: ResolveInfo,
        where: types.StarshipWhereUniqueInput = None,
    ):
        return filters.StarshipFilter(data=where).queryset

    def resolve_starship(
        _root: models.Starship,
        _info: ResolveInfo,
        where: types.StarshipWhereUniqueInput,
    ):
        return get_starship(where)


class Mutation(ObjectType):
    create_starship = CreateStarship.Field(required=True)
    update_starship = UpdateStarship.Field()
    delete_starship = DeleteStarship.Field()
