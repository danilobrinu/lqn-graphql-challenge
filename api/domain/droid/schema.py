# Built-in package
from typing import Annotated

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.droid import models, types
from api.domain.droid.data import create_droid, update_droid, delete_droid


class CreateDroid(types.DroidOutputMutation, Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _,
        info: ResolveInfo,
        data: Annotated[types.DroidCreateInput, "data used to create a new Droid"],
    ) -> Annotated[models.Droid, "returns a new Droid"]:
        return create_droid(data)


class UpdateDroid(types.DroidOutputMutation, Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _,
        info: ResolveInfo,
        where: Annotated[types.DroidWhereUniqueInput, "data used to get a Droid"],
        data: Annotated[types.DroidUpdateInput, "data used to update a Droid"],
    ) -> Annotated[models.Droid, "returns an updated Droid"]:
        return update_droid(where, data)


class DeleteDroid(types.DroidOutputMutation, Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _,
        info: ResolveInfo,
        where: Annotated[types.DroidWhereUniqueInput, "data used to get a Droid"],
    ) -> Annotated[models.Droid, "returns a deleted Droid"]:
        return delete_droid(where)


class DroidQuery(ObjectType):
    droid = Node.Field(types.Droid)
    droids = types.DroidFilterConnection(types.Droid, where=types.DroidWhereInput())


class DroidMutation(ObjectType):
    create_droid = CreateDroid.Field(required=True)
    update_droid = UpdateDroid.Field()
    delete_droid = DeleteDroid.Field()
