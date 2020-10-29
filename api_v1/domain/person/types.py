# Built-in packages

# Third-party packages
import graphene as gql
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.person import models, filters


class Person(DjangoObjectType):
    """A Person is a person related to the Episode sucn as a Director or Producer."""

    class Meta:
        model = models.Person
        filter_fields = []
        interfaces = (gql.Node,)


class PersonOutputMutation(gql.ObjectType):
    Output = Person


class PersonWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class PersonWhereInput(gql.InputObjectType):
    first_name = gql.String()
    first_name_not = gql.String()
    first_name_contains = gql.String()
    first_name_not_contains = gql.String()
    first_name_starts_with = gql.String()
    first_name_not_starts_with = gql.String()
    first_name_ends_with = gql.String()
    first_name_in = gql.String()
    first_name_not_in = gql.String()
    last_name = gql.String()
    last_name_not = gql.String()
    last_name_contains = gql.String()
    last_name_not_contains = gql.String()
    last_name_starts_with = gql.String()
    last_name_not_starts_with = gql.String()
    last_name_ends_with = gql.String()
    last_name_in = gql.String()
    last_name_not_in = gql.String()


class PersonCreateInput(gql.InputObjectType):
    first_name = gql.String(required=True)
    last_name = gql.String(required=True)


class PersonUpdateInput(gql.InputObjectType):
    first_name = gql.String()
    last_name = gql.String()


class PersonOneInput(gql.InputObjectType):
    connect = PersonWhereUniqueInput(required=True)


PersonFilterConnectionField = create_open_crud_filter_connection_field(
    "PersonFilterConnection", filters.PersonFilter
)
