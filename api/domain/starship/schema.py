# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.starship import models, types
from api.domain.starship.data import create_starship, update_starship, delete_starship


class CreateStarship(types.StarshipOutputMutation, Mutation):
    class Arguments:
        data = types.StarshipCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213
    def mutate(
        _root: models.Starship, _info: ResolveInfo, data: types.StarshipCreateInput
    ) -> models.Starship:
        return create_starship(data)


class UpdateStarship(types.StarshipOutputMutation, Mutation):
    class Arguments:
        where = types.StarshipWhereUniqueInput(required=True)
        data = types.StarshipUpdateInput(required=True)

    @atomic
    # skipcq: PYL-E0213
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
    # skipcq: PYL-E0213
    def mutate(
        _root: models.Starship,
        _info: ResolveInfo,
        where: types.StarshipWhereUniqueInput,
    ) -> models.Starship:
        return delete_starship(where)


class StarshipQuery(ObjectType):
    starship = Node.Field(types.Starship)
    starships = types.StarshipFilterConnectionField(
        types.Starship, where=types.StarshipWhereInput()
    )


class StarshipMutation(ObjectType):
    create_starship = CreateStarship.Field(required=True)
    update_starship = UpdateStarship.Field()
    delete_starship = DeleteStarship.Field()
