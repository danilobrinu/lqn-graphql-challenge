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

from .data import get_starship, create_starship, update_starship, delete_starship


class CreateStarship(types.StarshipOutputMutation, Mutation):
    class Input:
        data = types.StarshipCreateInput(required=True)

    @atomic
    def mutate(self, info, data: types.StarshipCreateInput):
        return create_starship(data)


class UpdateStarship(types.StarshipOutputMutation, Mutation):
    class Input:
        data = types.StarshipUpdateInput(required=True)
        where = types.StarshipWhereUniqueInput(required=True)

    @atomic
    def mutate(
        self,
        info,
        where: types.StarshipWhereUniqueInput,
        data: types.StarshipUpdateInput,
    ):
        return update_starship(where, data)


class DeleteStarship(types.StarshipOutputMutation, Mutation):
    class Input:
        where = types.StarshipWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, where: types.StarshipWhereUniqueInput):
        return delete_starship(where)


class StarshipQuery(ObjectType):
    starship = Node.Field(types.Starship)
    starships = types.StarshipFilterConnection(
        types.Starship, where=types.StarshipWhereInput()
    )


class StarshipMutation(ObjectType):
    create_starship = CreateStarship.Field(required=True)
    update_starship = UpdateStarship.Field()
    delete_starship = DeleteStarship.Field()
