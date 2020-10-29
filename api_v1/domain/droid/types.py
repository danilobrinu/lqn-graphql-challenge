# Built-in packages

# Third-party packages
import graphene as gql
from graphene_django import DjangoObjectType

# Local packages
from api_v1.utils.graphene import create_open_crud_filter_connection_field
from api_v1.domain.character.types import Character  # skipcq: PYL-W0611
from api_v1.domain.droid import models, filters


class Droid(DjangoObjectType, interfaces=(Character, gql.Node,)):
    """An object with an ID."""

    class Meta:
        model = models.Droid
        filter_fields = []


class DroidOutputMutation(gql.ObjectType):
    Output = Droid


class DroidWhereUniqueInput(gql.InputObjectType):
    id = gql.ID()


class DroidWhereInput(gql.InputObjectType):
    name = gql.String()
    name_not = gql.String()
    name_contains = gql.String()
    name_not_contains = gql.String()
    name_starts_with = gql.String()
    name_not_starts_with = gql.String()
    name_ends_with = gql.String()
    name_in = gql.String()
    name_not_in = gql.String()
    primary_function = gql.String()
    primary_function_not = gql.String()
    primary_function_contains = gql.String()
    primary_function_not_contains = gql.String()
    primary_function_starts_with = gql.String()
    primary_function_not_starts_with = gql.String()
    primary_function_ends_with = gql.String()
    primary_function_in = gql.String()
    primary_function_not_in = gql.String()


class DroidCreateInput(gql.InputObjectType):
    name = gql.String(required=True)
    primary_function = gql.String(required=True)


class DroidUpdateInput(gql.InputObjectType):
    name = gql.String()
    primary_function = gql.String()


DroidFilterConnectionField = create_open_crud_filter_connection_field(
    "DroidFilterConnection", filters.DroidFilter
)
