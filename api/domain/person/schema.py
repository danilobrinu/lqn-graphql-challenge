# Built-in package

# Third-party packages
from os import stat
from django.db.transaction import atomic
from graphene import ObjectType, Mutation, ResolveInfo
from graphene.relay import Node

# Local packages
from api.domain.person import models, types
from api.domain.person.data import create_person, update_person, delete_person


class CreatePerson(types.PersonOutputMutation, Mutation):
    class Arguments:
        data = types.PersonCreateInput(required=True)

    @atomic
    @staticmethod
    def mutate(_, info: ResolveInfo, data: types.PersonCreateInput) -> models.Person:
        return create_person(data)


class UpdatePerson(types.PersonOutputMutation, Mutation):
    class Arguments:
        data = types.PersonUpdateInput(required=True)
        where = types.PersonWhereUniqueInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _,
        info: ResolveInfo,
        where: types.PersonWhereUniqueInput,
        data: types.PersonUpdateInput,
    ) -> models.Person:
        return update_person(where, data)


class DeletePerson(types.PersonOutputMutation, Mutation):
    class Arguments:
        where = types.PersonWhereUniqueInput(required=True)

    @atomic
    @staticmethod
    def mutate(
        _, info: ResolveInfo, where: types.PersonWhereUniqueInput
    ) -> models.Person:
        return delete_person(where)


class PersonQuery(ObjectType):
    person = Node.Field(types.Person)
    persons = types.PersonFilterConnectionField(types.Person, where=types.PersonWhereInput())


class PersonMutation(ObjectType):
    create_person = CreatePerson.Field(required=True)
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()
