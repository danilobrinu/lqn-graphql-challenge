# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import Field, ObjectType, Mutation, ResolveInfo

# Local packages
from api_v1.domain.human import models, types
from api_v1.domain.human.data import get_human, create_human, update_human, delete_human


class CreateHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        data = types.HumanCreateInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human, info: ResolveInfo, data: types.HumanCreateInput
    ) -> models.Human:
        return create_human(data)


class UpdateHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        data = types.HumanUpdateInput(required=True)
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human,
        _info: ResolveInfo,
        where: types.HumanWhereUniqueInput,
        data: types.HumanUpdateInput,
    ):
        return update_human(where, data)


class DeleteHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    # skipcq: PYL-E0213, PYL-R0201
    def mutate(
        _root: models.Human, _info: ResolveInfo, where: types.HumanWhereUniqueInput
    ) -> models.Human:
        return delete_human(where)


class Query(ObjectType):
    human = Field(types.Human, where=types.HumanWhereUniqueInput(required=True))
    humans = types.HumanFilterConnectionField(
        types.Human, where=types.HumanWhereInput()
    )

    def resolve_human(
        _root: models.Human, _info: ResolveInfo, where: types.HumanWhereUniqueInput
    ):
        return get_human(where)


class Mutation(ObjectType):
    create_human = CreateHuman.Field(required=True)
    update_human = UpdateHuman.Field()
    delete_human = DeleteHuman.Field()
