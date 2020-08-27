# Built-in packages

# Third-party packages
from graphene import Node, ID, String
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType

# Local packages
from api.utils import create_open_crud_filter_connection
from . import models
from . import filters


class Person(DjangoObjectType):
    """A Person is a person related to the Episode sucn as a Director or Producer. """

    class Meta:
        model = models.Person
        filter_fields = []
        interfaces = (Node,)


class PersonOutputMutation(ObjectType):
    Output = Person


class PersonWhereUniqueInput(InputObjectType):
    id = ID()


class PersonWhereInput(InputObjectType):
    first_name = String()
    first_name_not = String()
    first_name_contains = String()
    first_name_not_contains = String()
    first_name_starts_with = String()
    first_name_not_starts_with = String()
    first_name_ends_with = String()
    first_name_in = String()
    first_name_not_in = String()
    last_name = String()
    last_name_not = String()
    last_name_contains = String()
    last_name_not_contains = String()
    last_name_starts_with = String()
    last_name_not_starts_with = String()
    last_name_ends_with = String()
    last_name_in = String()
    last_name_not_in = String()


class PersonCreateInput(InputObjectType):
    first_name = String(required=True)
    last_name = String(required=True)


class PersonUpdateInput(InputObjectType):
    first_name = String()
    last_name = String()


class PersonOneInput(InputObjectType):
    connect = PersonWhereUniqueInput(required=True)


PersonFilterConnection = create_open_crud_filter_connection(
    "PersonFilterConnection", filters.PersonFilter
)
