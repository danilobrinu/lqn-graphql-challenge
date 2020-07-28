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

from .data import get_droid, create_droid, update_droid, delete_droid


class CreateDroid(types.DroidOutputMutation, Mutation):
    class Input:
        data = types.DroidCreateInput(required=True)

    @atomic
    def mutate(self, info, data: types.DroidCreateInput):
        return create_droid(data)


class UpdateDroid(types.DroidOutputMutation, Mutation):
    class Input:
        data = types.DroidUpdateInput(required=True)
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    def mutate(
        self, info, where: types.DroidWhereUniqueInput, data: types.DroidUpdateInput,
    ):
        return update_droid(where, data)


class DeleteDroid(types.DroidOutputMutation, Mutation):
    class Input:
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, where: types.DroidWhereUniqueInput):
        return delete_droid(where)


class DroidQuery(ObjectType):
    droid = Node.Field(types.Droid)
    droids = types.DroidFilterConnection(types.Droid, where=types.DroidWhereInput())


class DroidMutation(ObjectType):
    create_droid = CreateDroid.Field(required=True)
    update_droid = UpdateDroid.Field()
    delete_droid = DeleteDroid.Field()
