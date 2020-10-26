# Built-in package

# Third-party packages
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.human import types
from api.domain.human.data import create_human, update_human, delete_human


class CreateHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        data = types.HumanCreateInput(required=True)

    @atomic
    def mutate(_, info: ResolveInfo, data: types.HumanCreateInput):
        return create_human(data)


class UpdateHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        data = types.HumanUpdateInput(required=True)
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    def mutate(
        _,
        info: ResolveInfo,
        where: types.HumanWhereUniqueInput,
        data: types.HumanUpdateInput,
    ):
        return update_human(where, data)


class DeleteHuman(types.HumanOutputMutation, Mutation):
    class Arguments:
        where = types.HumanWhereUniqueInput(required=True)

    @atomic
    def mutate(_, info: ResolveInfo, where: types.HumanWhereUniqueInput):
        return delete_human(where)


class HumanQuery(ObjectType):
    human = Node.Field(types.Human)
    humans = types.HumanFilterConnectionField(
        types.Human, where=types.HumanWhereInput()
    )


class HumanMutation(ObjectType):
    create_human = CreateHuman.Field(required=True)
    update_human = UpdateHuman.Field()
    delete_human = DeleteHuman.Field()
