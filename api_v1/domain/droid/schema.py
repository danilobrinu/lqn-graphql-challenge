# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from api_v1.domain.droid import models, types, crud


class CreateDroid(types.DroidOutputMutation, gql.Mutation):
    class Arguments:
        data = types.DroidCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Droid, _info: gql.ResolveInfo, data: types.DroidCreateInput,
    ) -> models.Droid:
        return crud.create_droid(data)


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
        return crud.update_droid(where, data)


class DeleteDroid(types.DroidOutputMutation, gql.Mutation):
    class Arguments:
        where = types.DroidWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Droid, _info: gql.ResolveInfo, where: types.DroidWhereUniqueInput,
    ) -> models.Droid:
        return crud.delete_droid(where)


class Query(gql.ObjectType):
    droid = gql.Field(types.Droid, where=types.DroidWhereUniqueInput(required=True))
    droids = gql.Field(
        gql.List(gql.NonNull(types.Droid)), where=types.DroidWhereInput()
    )

    def resolve_droid(
        _root: models.Droid, _info: gql.ResolveInfo, where: types.DroidWhereUniqueInput
    ) -> models.Droid:
        return crud.get_droid(where)

    def resolve_droids(
        _root: models.Droid, _info: gql.ResolveInfo, where: types.DroidWhereInput
    ) -> list[models.Droid]:
        return crud.get_droids(where)


class Mutation(gql.ObjectType):
    create_droid = CreateDroid.Field(required=True)
    update_droid = UpdateDroid.Field()
    delete_droid = DeleteDroid.Field()
