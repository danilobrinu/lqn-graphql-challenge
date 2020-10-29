# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from api_v1.domain.droid import models, types
from api_v1.domain.droid.data import get_droid, create_droid, update_droid, delete_droid


class CreateDroid(types.DroidOutputMutation, gql.Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Droid, _info: gql.ResolveInfo, data: types.DroidCreateInput,
    ) -> models.Droid:
        return create_droid(data)


class UpdateDroid(types.DroidOutputMutation, gql.Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)
        data = types.DroidUpdateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Droid,
        _info: gql.ResolveInfo,
        where: types.DroidWhereUniqueInput,
        data: types.DroidUpdateInput,
    ) -> models.Droid:
        return update_droid(where, data)


class DeleteDroid(types.DroidOutputMutation, gql.Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Droid, _info: gql.ResolveInfo, where: types.DroidWhereUniqueInput,
    ) -> models.Droid:
        return delete_droid(where)


class Query(gql.ObjectType):
    droid = gql.Field(types.Droid, where=types.DroidWhereUniqueInput(required=True))
    droids = types.DroidFilterConnectionField(
        types.Droid, where=types.DroidWhereInput()
    )

    def resolve_droid(
        _root: models.Droid, _info: gql.ResolveInfo, where: types.DroidWhereUniqueInput
    ):
        return get_droid(where)


class Mutation(gql.ObjectType):
    create_droid = CreateDroid.Field(required=True)
    update_droid = UpdateDroid.Field()
    delete_droid = DeleteDroid.Field()
