# Built-in package

# Third-party packages
import graphene as gql
from django.db.transaction import atomic

# Local packages
from . import models, types, crud


class CreateHuman(types.HumanOutputMutation, gql.Mutation):
    class Arguments:
        data = types.HumanCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human, info: gql.ResolveInfo, data: types.HumanCreateInput
    ) -> models.Human:
        return crud.create_human(data)


class UpdateHuman(types.HumanOutputMutation, gql.Mutation):
    class Arguments:
        data = types.HumanUpdateInput(required=True)
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human,
        _info: gql.ResolveInfo,
        where: types.HumanWhereUniqueInput,
        data: types.HumanUpdateInput,
    ):
        return crud.update_human(where, data)


class DeleteHuman(types.HumanOutputMutation, gql.Mutation):
    class Arguments:
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human, _info: gql.ResolveInfo, where: types.HumanWhereUniqueInput
    ) -> models.Human:
        return crud.delete_human(where)


class Query(gql.ObjectType):
    human = gql.Field(types.Human, where=types.HumanWhereUniqueInput(required=True))
    humans = gql.Field(
        gql.List(gql.NonNull(types.Human)), where=types.HumanWhereInput()
    )

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_human(
        _root: models.Human, _info: gql.ResolveInfo, where: types.HumanWhereUniqueInput
    ) -> models.Human:
        return crud.get_human(where)

    # skipcq: PYL-E0213, PYL-R0201
    def resolve_humans(
        _root: models.Human, _info: gql.ResolveInfo, where: types.HumanWhereInput
    ) -> list[models.Human]:
        return crud.get_humans(where)


class Mutation(gql.ObjectType):
    create_human = CreateHuman.Field(required=True)
    update_human = UpdateHuman.Field()
    delete_human = DeleteHuman.Field()
