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

from .data import get_person, create_person, update_person, delete_person


class CreatePerson(types.PersonOutputMutation, Mutation):
    class Input:
        data = types.PersonCreateInput(required=True)

    @atomic
    def mutate(self, info, data: types.PersonCreateInput):
        return create_person(data)


class UpdatePerson(types.PersonOutputMutation, Mutation):
    class Input:
        data = types.PersonUpdateInput(required=True)
        where = types.PersonWhereUniqueInput(required=True)

    @atomic
    def mutate(
        self, info, where: types.PersonWhereUniqueInput, data: types.PersonUpdateInput,
    ):
        return update_person(where, data)


class DeletePerson(types.PersonOutputMutation, Mutation):
    class Input:
        where = types.PersonWhereUniqueInput(required=True)

    @atomic
    def mutate(self, info, where: types.PersonWhereUniqueInput):
        return delete_person(where)


class PersonQuery(ObjectType):
    person = Node.Field(types.Person)
    persons = types.PersonFilterConnection(types.Person, where=types.PersonWhereInput())


class PersonMutation(ObjectType):
    create_person = CreatePerson.Field(required=True)
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()
