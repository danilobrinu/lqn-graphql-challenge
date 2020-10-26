# Built-in package

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
    def mutate(
        _root: models.Droid, _info: ResolveInfo, data: types.DroidCreateInput,
    ) -> models.Droid:
        return create_droid(data)


class UpdateDroid(types.DroidOutputMutation, Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    def mutate(
        _root: models.Droid,
        _info: ResolveInfo,
        where: types.DroidWhereUniqueInput,
        data: types.DroidUpdateInput,
    ) -> models.Droid:
        return update_droid(where, data)


class DeleteDroid(types.DroidOutputMutation, Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    def mutate(
        _root: models.Droid, _info: ResolveInfo, where: types.DroidWhereUniqueInput,
    ) -> models.Droid:
        return delete_droid(where)


class DroidQuery(ObjectType):
    droid = Node.Field(types.Droid)
    droids = types.DroidFilterConnectionField(
        types.Droid, where=types.DroidWhereInput()
    )


class DroidMutation(ObjectType):
    create_droid = CreateDroid.Field(required=True)
    update_droid = UpdateDroid.Field()
    delete_droid = DeleteDroid.Field()
